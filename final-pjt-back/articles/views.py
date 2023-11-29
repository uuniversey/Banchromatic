from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment, Question, CommentQA
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, QuestionSerializer, QuestionListSerializer, CommentQASerializer

# 게시글 조회, 생성, 삭제, 수정, 좋아요(저장)
# 댓글 생성, 삭제
# 권한에 따라 다른 동작 (본인이 작성한 게시글 및 댓글만 삭제)

# article
# 게시글 조회(게시판 메인 페이지) / 생성 
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 조회(게시글 상세 페이지) / 삭제 / 수정
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def question_list(request):

    if request.method == 'GET':
        questions = get_list_or_404(Question)
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# -------------------------------------------------

# comment
# 댓글 목록 조회
@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 단일 댓글 조회 / 삭제 / 수정
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 댓글 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# ------------------------------------------------------------------------------
# qacomment
# 댓글 목록 조회
@api_view(['GET'])
def qa_comment_list(request):
    comments = get_list_or_404(CommentQA)
    serializer = CommentQASerializer(comments, many=True)
    return Response(serializer.data)


# 단일 댓글 조회 / 삭제 / 수정
@api_view(['GET', 'DELETE', 'PUT'])
def qa_comment_detail(request, comment_pk):
    comment = get_object_or_404(CommentQA, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentQASerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentQASerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 댓글 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def qa_comment_create(request, article_pk):
    article = get_object_or_404(Question, pk=article_pk)
    serializer = CommentQASerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)