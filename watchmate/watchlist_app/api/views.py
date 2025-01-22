from rest_framework.response import Response
# from rest_framework.decorators import api_view
from watchlist_app.models import WatchList, StreamingPlatform
from watchlist_app.api.serializers import WatchlistSerializer, StreamingPlatformSerializer
from rest_framework import status
from rest_framework.views import APIView


class StreamingPlatformAV(APIView):
    def get(self, request):
        platforms = StreamingPlatform.objects.all()  # Corrected query
        serializer = StreamingPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListAV(APIView):
    def get(self, request):
        watchlists = WatchList.objects.all()  # Corrected query
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)  # Corrected query
        except WatchList.DoesNotExist:  # Corrected model name
            return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(watchlist)  # Corrected serializer usage
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)  # Corrected query
        except WatchList.DoesNotExist:  # Corrected model name
            return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(watchlist, data=request.data)  # Corrected serializer usage
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)  # Corrected query
        except WatchList.DoesNotExist:  # Corrected model name
            return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)

        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamingPlatformdetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

           






# @api_view(['GET','POST'])
# def Watchlist_list(request):
#     if request.method == 'GET':
#         Watchlists = Watchlist.objects.all()
#         serializer = WatchlistSerializer(Watchlists , many = True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])   
# def Watchlist_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             Watchlist = Watchlist.objects.get(pk=pk)
#         except Watchlist.DoesNotExist:
#             return Response({'error':'Watchlist not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchlistSerializer(Watchlist)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         Watchlist = Watchlist.objects.get(pk=pk)
#         serializer = WatchlistSerializer(Watchlist,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         Watchlist = Watchlist.objects.get(pk=pk)
#         Watchlist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)