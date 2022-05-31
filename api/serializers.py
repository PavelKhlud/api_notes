from django.contrib.auth import get_user_model
from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api:note-detail')

    @staticmethod
    def get_author(obj):
        return str(obj.author.email)

    class Meta:
        model = Note
        fields = ['id', 'title', 'text', 'author', 'url']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'email', 'name', 'password', 'is_admin')
        extra_kwargs = {'passwrd': {'write_only': True}}

    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'), instance.get('password'))
        return super().update(instance, validated_data)

