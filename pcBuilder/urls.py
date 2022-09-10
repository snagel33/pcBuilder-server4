from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from pcBuilderapi.views import register_user, login_user
from rest_framework import routers
from pcBuilderapi.views import PartTypeView, PartView, BuildView, BuilderView, BuildPartView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'partTypes', PartTypeView, 'partType')
router.register(r'parts', PartView, 'part')
router.register(r'builds', BuildView, 'build')
router.register(r'builders', BuilderView, 'builder')
router.register(r'buildParts', BuildPartView, 'buildPart')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]