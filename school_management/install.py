# school_management/install.py
import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def after_install():
    """Executes after app installation"""
    add_custom_fields()
#    create_default_roles()
    
def add_teacher_field():
    """Add is_teacher checkbox to Employee"""
    if not frappe.db.exists("Custom Field", {"dt": "Employee", "fieldname": "is_teacher"}):
        create_custom_field(df={
            "dt": "Employee",
            "label": _("Is Teacher"),
            "fieldname": "is_teacher",
            "fieldtype": "Check",
            "insert_after": "employment_type",
            "description": _("Identifies teaching staff"),
            "default": 0
        })
        frappe.db.commit()

def add_custom_fields():
    # Check if the custom field already exists
    if not frappe.db.exists("Custom Field", "Employee-is_teacher"):
        custom_fields = {
            "Employee": [
                dict(
                    fieldname='is_teacher',
                    label='Is Teacher',
                    fieldtype='Check',
                    insert_after='employee_type',
                    default=0
                )
            ]
        }
        create_custom_field(custom_fields)
        frappe.db.commit()  # Commit to ensure changes are saved

def create_default_roles():
    """Create Teacher role if not exists"""
    if not frappe.db.exists("Role", "Teacher"):
        doc = frappe.new_doc("Role")
        doc.update({
            "role_name": "Teacher",
            "desk_access": 1,
            "is_custom": 1
        })
        doc.insert(ignore_permissions=True)
