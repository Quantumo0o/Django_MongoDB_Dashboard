from rest_framework import serializers
from myapp.models import Insight

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = '__all__'  # or specify individual fields if needed

class AggregatedInsightsSerializer(serializers.Serializer):
    country = serializers.CharField()
    topic = serializers.CharField()
    total_intensity = serializers.FloatField()
    total_likelihood = serializers.FloatField()
    total_relevance = serializers.FloatField()