from rest_framework import serializers
from .models import Article, Comment, Question, CommentQA
from django.contrib.auth import get_user_model

class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content',)
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = ('id', 'title', 'content',)
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('user',)
        read_only_fields = ('article', 'user')



class CommentQASerializer(serializers.ModelSerializer):
    # class ArticleSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Article
    #         fields = ('title',)
            
    # article = ArticleSerializer(read_only=True)

    class Meta:
        model = CommentQA
        fields = '__all__'
        # read_only_fields = ('user',)
        read_only_fields = ('article', 'user')
