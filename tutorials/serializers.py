from rest_framework import serializers 
from tutorials.models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'Book_title',
                  'Book_author',
                  'Page_numbers',
                  'Prize',
                  'Ratings',
                  )