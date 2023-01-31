# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Product Template Link On Variant",
    "summary": """This module is used to provide a direct link from the product variant to the product template.""",
    "version": "15.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        'base',
        'product',
    ],
    "data": [
        "views/product_views.xml",
    ],
    "cloc_exclude": [
        "**/*", # can be used to ignore an entire module.
    ],
}
