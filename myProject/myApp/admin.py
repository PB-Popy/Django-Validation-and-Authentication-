from django.contrib import admin
from myApp.models import *

admin.site.register(CustomUser)
admin.site.register(ResumeModel)
admin.site.register(LanguageModel)
admin.site.register(IntermediateLanguageModel)
admin.site.register(IntermediateSkillModel)
admin.site.register(SkillModel)
