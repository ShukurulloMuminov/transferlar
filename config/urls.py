from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

def home(request):
    return HttpResponse("Sayt ishlayapti 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('latest-transfer/', LatestClubsView.as_view(), name='latest-transfer'),
    path('players/', PlayersView.as_view(), name='players'),
    path('player_u20/', Player_U20View.as_view(), name='player_u20'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
