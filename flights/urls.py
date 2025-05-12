from django.urls import path
from .views import FlightListCreateView, FlightRetrieveView, GateListCreateView, GateRetrieveView, PassengerListCreateView, PagessengerRetrieveView, FlightReportAPIView, PassengerRerpotAPIView, GateReportAPIView

urlpatterns = [
    path('flights/', FlightListCreateView.as_view(), name='flights'),
    path('flights/<int:pk>/', FlightRetrieveView.as_view(), name='flight'),
    path('flights/today/', FlightReportAPIView.as_view(), name='flight_report'),
    path('flights/<int:pk>/passengers/', PassengerRerpotAPIView.as_view(), name='flight_passengers'),
    path('flights/gates/', GateReportAPIView.as_view(), name='flight_gates'),
    path('passengers/<int:pk>/', PagessengerRetrieveView.as_view(), name='passenger'),
    path('gates/', GateListCreateView.as_view(), name='gates'),
    path('gates/<int:pk>/', GateRetrieveView.as_view(), name='gate')
]