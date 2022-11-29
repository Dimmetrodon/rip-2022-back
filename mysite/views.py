from rest_framework import viewsets
from mysite.serializers import ApartmentsSerializer, UsersSerializer, ApartmentSellSerializer
from mysite.models import Apartments, Users, ApartmentSell


class ApartmentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    serializer_class = ApartmentsSerializer  # Сериализатор для модели

    def get_queryset(self):
        queryset = Apartments.objects.all()
        if self.request.method == 'GET':
            params = self.request.query_params.dict()
            try:
                if params['q'] == 'all':
                    pass
                else:
                    queryset = queryset.filter(name__icontains=params['q'])
            except:
                pass
            try:
                queryset = queryset.filter(cost__lte=params['max_cost'])
            except:
                pass
            try:
                queryset = queryset.filter(cost__gte=params['min_cost'])
            except:
                pass
        return queryset.order_by('name')



class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Users.objects.all().order_by('user_name')
    serializer_class = UsersSerializer  # Сериализатор для модели


class ApartmentSellViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = ApartmentSell.objects.all().order_by('post_date').prefetch_related()
    serializer_class = ApartmentSellSerializer  # Сериализатор для модели
