# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "myproducts"
app_title = "myproducts"
app_publisher = "Ahmed"
app_description = "myproducts"
app_icon = "myproducts"
app_color = "grey"
app_email = "final.option@hotmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = ["/assets/myproducts/css/bootstrap.css",
#                    "/assets/myproducts/css/font-awesome/css/font-awesome.css"
#                    ]
# app_include_js = "/assets/myproducts/js/myproducts.js"

# include js, css files in header of web template
web_include_css = ["/assets/myproducts/css/bootstrap.css",
                   "/assets/myproducts/css/font-awesome/css/font-awesome.css"
                  ]
# web_include_js = "/assets/myproducts/js/myproducts.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "myproducts.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "myproducts.install.before_install"
# after_install = "myproducts.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "myproducts.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"myproducts.tasks.all"
# 	],
# 	"daily": [
# 		"myproducts.tasks.daily"
# 	],
# 	"hourly": [
# 		"myproducts.tasks.hourly"
# 	],
# 	"weekly": [
# 		"myproducts.tasks.weekly"
# 	]
# 	"monthly": [
# 		"myproducts.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "myproducts.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "myproducts.event.get_events"
# }

