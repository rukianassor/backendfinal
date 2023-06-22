from django.urls import path
from app.views import AboutView, ContactView, CosmeticView, LoginView, MedicineView, OrderView, PharmacyView, MedicineInfo

urlpatterns = [
    path('med/', MedicineView.as_view()),
    path('med/<int:id>/',MedicineInfo.as_view()),
    path('cos/', CosmeticView.as_view()),
    path('order/', OrderView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('pham/', PharmacyView.as_view()),

]
