from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

# swagger object
schema_view = get_swagger_view(title='Flight Reservation API')

urlpatterns = [
    #     documentation
    path('documentation/', schema_view),
    path('docs/', include_docs_urls(title='Flight Reservation API(Core)')),

    path('admin/', admin.site.urls),
    path('api/', include('flightAPP.urls')),
]
