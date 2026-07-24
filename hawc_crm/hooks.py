from . import __version__ as app_version

app_name = "hawc_crm"
app_title = "HAWC CRM"
app_publisher = "Developer"
app_description = "CRM app for HAWC"
app_email = "dev@example.com"
app_license = "mit"

doc_events = {
	"Lead": {
		"on_update": "hawc_crm.api.auto_create_deal"
	},
	"Deal": {
		"on_update": "hawc_crm.api.notify_manager_on_won"
	}
}
