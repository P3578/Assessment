from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet,Comment
from .serializers import SnippetSerializer,CommentSerializer

# Create your views here.
@api_view(['GET','POST'])
def snippet_list(request,format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=204)
    
@api_view(['GET','POST'])
def comment_list(request,format=None):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)