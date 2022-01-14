from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import PostSerializer

# Create your views here.
class NoteListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = PostSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = PostSerializer
    