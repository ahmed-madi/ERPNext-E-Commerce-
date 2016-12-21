
# -*- coding: utf-8 -*-
# Copyright (c) 2015, Omar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document
from frappe.auth import LoginManager



def get_context(context):
    context.list_items = frappe.get_list('Shopping' ,'*')

@frappe.whitelist(allow_guest=True)
def addToShopcart(id, qty, price):
    #return qty
    #return id
	# if frappe.db.exists("Lead", {"email_id": email}):
	# 	return -1S
    item = frappe.get_list("Item", "*",filters={"item_code": id})
    # return item
    if item:
        quant = float(item[0].quantity)
        qty = int(qty)
        # return item[0].description
        if qty > quant:
            msg = "The quantity you inserted is greater than available"
            return msg
        elif qty == "" or 0:
            msg = "Please insert a quantity"
            return msg
        # return item[0].item_name
        else:
            # child = {
            #     "item_code": item[0].item_code,
            #     "item_name": item[0].item_name,
            #     "description": item[0].description,
            #     "qty": quant,
            #     "image": item[0].thumbnail
            # }
            price = int(price)
            total = price * qty
            #owner = print frappe.session.user
            shopping =  frappe.get_doc({
                "doctype": "Shopping",
                "item_code": item[0].item_code,
                "item_name": item[0].item_name,
                "description": item[0].description,
                "qty": qty,
                "item_group": item[0].item_name,
                "image": item[0].thumbnail,
                "price": price,
                "total_price": total,
                "owner": "DD"
            })
            shopping.insert(ignore_permissions = True)
            #frappe.db.set_value("Item","Item", "quantity", quant - qty)
            query = "update `tabItem` set quantity={0} where item_code={1}".format(quant-qty, id)
            frappe.db.sql(query)
            frappe.db.commit()
            #frappe.db.set_value(self, dt, dn, field, val, modified=None, modified_by=None, update_modified=True, debug=False)
            return 1
    else:
        msg = "No such item available"
        return msg

