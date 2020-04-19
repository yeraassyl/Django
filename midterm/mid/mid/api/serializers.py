from rest_framework import serializers
from mid.api.models import Book,Journal

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'price', 'description', 'num_pages', 'genre', 'created_at')

    def validate_num_pages(self,value):
        if value < 0:
            raise serializers.ValidationError('num_pages can not be negative')
        return value


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'price', 'description', 'publisher', 'type', 'created_at')

    def validate_type(self,value):
        TYPE_FIELDS = (
            1,2,3,4
        )

        if value not in TYPE_FIELDS:
            raise serializers.ValidationError('invalid journal type')
        return value