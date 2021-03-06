from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dailybey.models import Article
from dailybey.serializers import ArticleSerializer

@api_view(['GET'])
def home(request):
    return render(request, "templates/home.html")


@api_view(['GET', 'POST'])
def list_all_articles(request):
    if request.method == 'GET':
        all_articles = Article.objects.all()
        serializer = ArticleSerializer(all_articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def list_single_article_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        single_article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(single_article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(single_article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        single_article.delete()
        return HttpResponse(status=204)