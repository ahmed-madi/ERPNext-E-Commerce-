# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

base_template_path = "stock.html"

import os, re
import frappe
from frappe import _

def get_context(context):

    # context.items = frappe.get_list('Item' ,'item_name,item_group,item_code,quantity')
    # context.items_price = frappe.get_list('Item Price', 'price_list_rate')

    raw = frappe.db.sql("""SELECT tabItem.item_name, tabItem.item_group, tabItem.thumbnail, tabItem.quantity,
 `tabItem Price`.price_list_rate, tabItem.item_code, tabItem.name from tabItem
                  INNER JOIN `tabItem Price` ON tabItem.item_code = `tabItem Price`.item_code""")

    context.items = list(raw)

#context.items_price = frappe.get_list('Item Price','item_code')
#	return { "doc": frappe.get_doc('Item') }
#context.items = frappe.get_list('Item','item_name,item_group' )

