from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="KAFE API",
        default_version='v1',
        description="Bu API uchun Swagger hujjati",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xtuxtamirzayev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    # generator_class = JWTSchemaGenerator

)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('products.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
