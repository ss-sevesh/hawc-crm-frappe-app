import frappe

@frappe.whitelist(allow_guest=False)
def get_all_leads():
	return frappe.get_all("Lead", fields=["name", "lead_name", "status", "assigned_to"])

@frappe.whitelist(allow_guest=False)
def create_lead(lead_name, email, phone=None, source="Other", status="New"):
	doc = frappe.new_doc("Lead")
	doc.lead_name = lead_name
	doc.email = email
	doc.phone = phone
	doc.source = source
	doc.status = status
	doc.insert()
	frappe.db.commit()
	return doc.name

@frappe.whitelist(allow_guest=False)
def get_pipeline():
	deals = frappe.get_all("Deal", fields=["name", "deal_title", "deal_value", "stage"])
	pipeline = {}
	for deal in deals:
		stage = deal.stage
		if stage not in pipeline:
			pipeline[stage] = []
		pipeline[stage].append(deal)
	return pipeline

@frappe.whitelist(allow_guest=False)
def convert_lead_to_deal(lead_name, deal_value, expected_close_date=None):
	lead = frappe.get_doc("Lead", lead_name)
	
	deal = frappe.new_doc("Deal")
	deal.deal_title = f"Deal with {lead.company_name or lead.lead_name}"
	deal.lead = lead.name
	deal.contact_name = lead.lead_name
	deal.company = lead.company_name
	deal.deal_value = deal_value
	if expected_close_date:
		deal.expected_close_date = expected_close_date
	deal.stage = "Prospecting"
	deal.assigned_to = lead.assigned_to
	deal.insert()
	
	lead.status = "Qualified"
	lead.save()
	frappe.db.commit()
	return deal.name

@frappe.whitelist(allow_guest=False)
def get_activity_summary():
	activities = frappe.get_all("Activity Log", fields=["activity_type"])
	summary = {}
	for activity in activities:
		atype = activity.activity_type
		summary[atype] = summary.get(atype, 0) + 1
	return summary

def auto_create_deal(doc, method):
	if doc.status == "Qualified":
		# check if deal already exists for this lead
		existing = frappe.get_all("Deal", filters={"lead": doc.name})
		if not existing:
			deal = frappe.new_doc("Deal")
			deal.deal_title = f"Deal with {doc.company_name or doc.lead_name}"
			deal.lead = doc.name
			deal.contact_name = doc.lead_name
			deal.company = doc.company_name
			deal.deal_value = 0 # Default 0, needs manual update
			deal.stage = "Prospecting"
			deal.assigned_to = doc.assigned_to
			deal.insert()

def notify_manager_on_won(doc, method):
	if doc.stage == "Closed Won":
		# For demonstration, notify CRM Manager users
		managers = frappe.get_all("Has Role", filters={"role": "CRM Manager", "parenttype": "User"}, fields=["parent"])
		recipients = [m.parent for m in managers]
		if recipients:
			frappe.sendmail(
				recipients=recipients,
				subject=f"Deal Won: {doc.deal_title}",
				message=f"Deal {doc.name} worth {doc.deal_value} was won!"
			)
