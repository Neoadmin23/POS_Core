from __future__ import annotations

import frappe
import frappe.sessions

no_cache = 1


def get_context(context):
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login?redirect-to=/alphax-pos"
        raise frappe.Redirect
    context.csrf_token = frappe.sessions.get_csrf_token()
    frappe.db.commit()  # nosemgrep
    context.no_cache = 1
    context.show_sidebar = False
    return context
