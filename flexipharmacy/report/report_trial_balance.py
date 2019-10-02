# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError
from datetime import datetime


class report_trial_balance(models.AbstractModel):
    _name = 'report.flexipharmacy.trial_balance_template'
    _description = 'report_trial_balance'

    def _get_init_bal(self, from_date, company_id, account_id):
        if from_date and company_id and account_id:
            account_config_id = self.env['res.config.settings'].search([], order='id desc', limit=1)
            current_year = datetime.strptime(from_date, '%Y-%m-%d').year
            fiscal_year_start_date = ''
            if account_config_id and account_config_id.fiscalyear_last_month and account_config_id.fiscalyear_last_day:
                fiscal_month = account_config_id.fiscalyear_last_month
                fiscal_end_date = account_config_id.fiscalyear_last_day
                if fiscal_month == 12:
                    current_year -= 1
                fiscal_year_start_date = str(current_year) + '-' + str(fiscal_month) + '-' + str(fiscal_end_date)
                fiscal_year_start_date = datetime.strftime(datetime.strptime(fiscal_year_start_date, '%Y-%m-%d') + timedelta(days=1), '%Y-%m-%d')
            else:
                fiscal_year_start_date = str(current_year) + '-01-01'
            SQL = """select sum(aml.debit) as debit, sum(aml.credit) as credit
                    FROM account_move_line aml,account_move am
                    WHERE 
                    aml.move_id = am.id AND
                    aml.account_id = %s
                    AND aml.company_id = %s
                    AND aml.date::timestamp::date < '%s'
                    AND am.state = 'posted'
                    """ % (account_id, company_id, str(from_date))
            self._cr.execute(SQL)
            result = self._cr.dictfetchall()
        if result and result[0].get('debit') and result[0].get('credit'):
            result = [result[0].get('debit'), result[0].get('credit'), result[0].get('debit') - result[0].get('credit')]
        elif result and result[0].get('debit') and not result[0].get('credit'):
            result = [result[0].get('debit'), 0.0, result[0].get('debit') - 0.0]
        elif result and not result[0].get('debit') and result[0].get('credit'):
            result = [0.0, result[0].get('credit'), 0.0 - result[0].get('credit')]
        else:
            result = [0.0, 0.0, 0.0]
        return result

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
 
        account_result = {}
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_ids', []))
        display_account = data['form'].get('display_account') 
        accounts = self.env['account.account'].search([])
        date_from = data.get('form') and data.get('form').get('date_from')
        date_to = data.get('form') and data.get('form').get('date_to')
        state = data['form'] and data['form']['target_move']
        
        SQL = """ 
            SELECT 
              am.id as move_id, 
              am.date as date, 
              aml.debit as debit, 
              aml.credit as credit,
              aml.balance as balance,
              aml.account_id as id
            FROM 
              account_move as am, 
              account_move_line as aml"""
        where_clause = """
            WHERE 
              am.id = aml.move_id AND
              aml.account_id in %s
        """% (" (%s) " % ','.join(map(str, accounts.ids)))

        if date_from:
            where_clause += "AND am.date >= '%s' "% (date_from)
        if date_to:
            where_clause += "AND am.date <= '%s' "% (date_to)
        if state and state == 'posted':
            where_clause += "AND am.state = '%s' "% (state)
        self.env.cr.execute(SQL + where_clause)
        res = self.env.cr.dictfetchall()
        for row in res:
            account_result[row.pop('id')] = row

        account_res = []
        for account in accounts:
            res = dict((fn, 0.0) for fn in ['credit', 'debit', 'balance'])
            currency = account.currency_id and account.currency_id or account.company_id.currency_id
            res['code'] = account.code
            res['name'] = account.name
            if account.id in account_result.keys():
                res['debit'] = account_result[account.id].get('debit')
                res['credit'] = account_result[account.id].get('credit')
                res['balance'] = account_result[account.id].get('balance')
            if date_from and data['form'] and data['form']['include_init_balance']:
                init_bal = self._get_init_bal(date_from, account.company_id.id, account.id)
                res['init_bal'] = init_bal[2]
            if display_account == 'all':
                account_res.append(res)
            if display_account == 'not_zero' and not currency.is_zero(res['balance']):
                account_res.append(res)
            if display_account == 'movement' and (not currency.is_zero(res['debit']) or not currency.is_zero(res['credit'])):
                account_res.append(res)

        return {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data,
            'docs': docs,
            'time': time,
            'Accounts': account_res,
        }
