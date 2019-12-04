from django.urls import path, include
from Assistant.views import GrammerCheckView, PosView


urlpatterns = [
    path('check/', GrammerCheckView.as_view()),
    path('pos/', PosView.as_view()),
]
