from django.conf.urls import url, include
from rest_framework import routers
from spa_gastos.gastos import views

router = routers.DefaultRouter()
router.register(r'gastos', views.GastosViewSet, 'gastos')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
        url(r'^', include(router.urls)),
 ]
