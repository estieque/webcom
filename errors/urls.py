from django.conf.urls import handler400, handler403, handler404, handler500
from .views import custom_400_view, custom_403_view, custom_404_view, custom_500_view

urlpatterns = [
    
]
handler400 = custom_400_view
handler403 = custom_403_view
handler404 = custom_404_view
handler500 = custom_500_view
