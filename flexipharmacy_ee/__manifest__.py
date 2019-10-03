# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'POS Pharmacy',
    'version': '1.0.0',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'summary': 'POS Pharmacy with Responsive Design (Community)',
    'description': "POS Pharmacy with Responsive Design (Community)",
    'category': 'Point Of Sale',
    'website': 'http://www.acespritech.com',
    'depends': ['base', 'point_of_sale', 'stock', 'sale_stock', 'sale_management', 'barcodes', 'product_expiry',
                'purchase', 'hr_attendance', 'account'],
    'price': 170.00,
    'currency': 'EUR',
    'images': [
        'static/description/main_screenshot.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/reservation_data.xml',
        'data/pos_cache_data.xml',
        'data/product_expiry_scheduler.xml',
        'data/product_alert_email_template.xml',
        'data/customer_schedular.xml',
        'views/res_config_setting_view.xml',
        'views/flexipharmacy_ee.xml',
        'views/res_config_settings.xml',
        'views/generate_product_barcode_view.xml',
        'views/point_of_sale.xml',
        'views/pos_config.xml',
        'views/res_config_settings.xml',
        'views/sale_view.xml',
        'views/pos_shop_view.xml',
        'views/stock.xml',
        'views/pos_cache_views.xml',
        'views/product_view.xml',
        'views/product_brand_view.xml',
        'views/account_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/gift_card.xml',
        'views/voucher_view.xml',
        'views/voucher_code_sequence.xml',
        'views/res_users_view.xml',
        'views/pos_sales_report_template.xml',
        'views/pos_sales_report_pdf_template.xml',
        'views/sales_details_pdf_template.xml',
        'views/sales_details_template.xml',
        'views/front_sales_report_pdf_template.xml',
        'views/front_sales_thermal_report_template.xml',
        'reports.xml',
        'views/front_inventory_session_pdf_report_template.xml',
        'views/front_inventory_session_thermal_report_template.xml',
        'views/front_inventory_location_pdf_report_template.xml',
        'views/front_inventory_location_thermal_report_template.xml',
        'wizard/wizard_pos_sale_report_view.xml',
        'wizard/wizard_sales_details_view.xml',
        'wizard/wizard_pos_x_report.xml',
        'views/pos_z_report_template.xml',
        'views/pos_z_thermal_report.xml',
        'views/pos_x_thermal_report.xml',
        'views/pos_promotion_view.xml',
        'views/stock_production_lot_view.xml',
        'views/wallet_management_view.xml',
        'views/cash_inout_menu.xml',
        'views/customer_display.xml',
        'views/dashboard.xml',
        'views/recurrent_order.xml',
        'views/delivery_order_screen.xml',

        # Commission Part Started
        # Note: Other Views are added in existing ones.
        'views/pos_agent_commission _view.xml',
        'report/pos_report_agent_payment.xml',
        'report/pos_agent_payment_report_template.xml',
        'wizard/pos_agent_commission_payment_view.xml',
        'views/non_moving_product_report.xml',
        'wizard/non_moving_stock.xml',
        'report/grp_category_product_expiry_report_template.xml',
        'wizard/product_expiry_report_wizard_view.xml',
        'views/product_expiry_report_view.xml',
        'data/send_mail.xml',

        # Commission Part Ended
    ],
    'post_init_hook': 'post_init',
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
