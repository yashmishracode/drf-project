from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform

class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = "__all__"

class WatchlistSerializer(serializers.ModelSerializer):
    
    # lan_name = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = "__all__"
        # field = ['name','discription','active']
        # exclude = ["active"]
        
    # def get_lan_name(self,object):
    #     return len(object.name)
        



# class WatchlistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     discription = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Watchlist.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.discription = validated_data.get('discription',instance.discription)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance