# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bank_integration"
app_title = "Bank Integration"
app_publisher = "Resilient Tech"
app_description = "Unofficial API to handle bank transactions using ERPNext"
app_icon = "fa fa-university"
app_color = "#f77174"
app_email = "info@resilient.tech"
app_license = "MIT"

after_install = "bank_integration.install.after_install"

# app_include_js = "assets/bank_integration/js/common.js"

doctype_js = {
    "Payment Entry": "public/js/payment_entry.js",
    "Bank Account": "public/js/bank_account.js",
    "Bank Reconciliation Tool": "public/js/bank_reconciliation_tool.js"
}

page_js = {
    "bank-reconciliation": "public/js/bank_reconciliation.js",
}
