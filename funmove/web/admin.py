from django.contrib import admin

# Register your models here.
from models.member import BackAdmin

# Register your models here.
class BackAdminAdmin(admin.ModelAdmin):
	# Display in Admin
	list_display = ["__unicode__", "create_date", "update_date"]
	# Edit Model field (by Form)
	# form = OnlineQuestionForm

	class Meta:
		model = BackAdmin

# reigster model and set the Admin custom by second args
admin.site.register(BackAdmin, BackAdminAdmin)