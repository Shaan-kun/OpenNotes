from django.urls import path
from .views import *

urlpatterns = [
    path('', JournalListView.as_view(), name='home'),
    path('journal/list', JournalListView.as_view(), name="journal-list"),
    path('journal/journal-create', JournalCreateView.as_view(), name="create-journal"),
    path('journal/journal-update/<pk>', JournalUpdateView.as_view(), name="update-journal"),
    path('journal/journal-delete/<pk>', JournalDeleteView.as_view(), name="delete-journal"),
]
