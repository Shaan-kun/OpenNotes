from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class JournalListView(ListView):
    model = Journal
    template_name = 'journal/journal_list.html'
    context_object_name = 'journal_list'


class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal/create_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journal-list')


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'journal/update_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journal-list')


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal/delete_journal_form.html'
    success_url = reverse_lazy('journal-list')
