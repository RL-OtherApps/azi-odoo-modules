# -*- coding: utf-8 -*-
# (c) 2017 Matt Taylor

{
    "name": "Serial CRM",
    "version": "10.0.1",
    "summary": "Extra Info for Serialized Products",
    "category": "Inventory",
    "author": "Chris Emigh",
    "website": "http://www.github.com/asphaltzipper",
    'description': """
        Add fields for additional info and for linking serials with customers
    """,
    "depends": [
        "base",
        "stock",
        "mrp",
        "stock_inventory_revaluation",
        "attachment_priority",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/stock_lot_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    "installable": True,
    "auto_install": False,
}
