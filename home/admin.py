from django.contrib import admin
from .models import contests
from .models import user_details
from .models import questions
from .models import answers
from .models import scoring
from .models import tests
from .models import choices
from .models import editor_themes
from .models import editor_language

admin.site.register(contests)
admin.site.register(user_details)
admin.site.register(questions)
admin.site.register(answers)
admin.site.register(scoring)
admin.site.register(tests)
admin.site.register(choices)
admin.site.register(editor_themes)
admin.site.register(editor_language)