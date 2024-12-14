from rest_framework import serializers
from drfsiti.models import Women
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drfsiti.models import Women

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    contend = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.contend = validated_data.get("contend", instance.contend)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)

        # Работа с ForeignKey
        cat_id = validated_data.get("cat_id")
        if cat_id:
            instance.cat_id = cat_id  # Используем .cat_id для сохранения id категории

        instance.save()
        return instance





class WomenCreateView(APIView):
    def post(self, request):
        # Сериализация данных из запроса
        serializer = WomenSerializer(data=request.data)

        if serializer.is_valid():
            # Сохраняем данные в базе данных
            serializer.save()
            # Возвращаем ответ с созданными данными
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Возвращаем ошибки валидации, если есть
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


