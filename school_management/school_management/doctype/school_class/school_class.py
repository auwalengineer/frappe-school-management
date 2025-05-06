# Copyright (c) 2025, Auwal Isiaku Mafindi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SchoolClass(Document):
    pass


@frappe.whitelist()
def get_class_arms(class_level):
    """Safe method to fetch arms for a class level"""
    if not frappe.has_permission("Class Level", "read"):
        frappe.throw("Not permitted", frappe.PermissionError)
    
    arms = frappe.get_all(
        "Class Arm",
        filters={"parent": class_level},
        pluck="arm"
    )
    return arms
