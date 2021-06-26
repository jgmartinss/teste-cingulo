from calendar import monthrange

from django.db.models import Q

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import UserActivities


class UserActivitiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        qs = UserActivities.objects.filter(Q(id_user=pk)).values(
            "id_user", "ref_year", "data"
        )

        return Response(data=qs, status=status.HTTP_200_OK)


class UsersActivitiesByDateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, date=None):
        qs = UserActivities.objects.filter(Q(data__contains={date: 1})).count()

        return Response(data={"total": qs}, status=status.HTTP_200_OK)


class UsersActivitiesByMonthView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, year=None, month=None):
        data = {}

        for item in range(1, monthrange(int(year), int(month))[1]):
            date = f'{year}-{month}-0{item}' if item < 10 else f'{year}-{month}-{item}'
            data.update(
                {
                    date: UserActivities.objects.filter(
                        Q(ref_year=year), Q(data__contains={date: 1})
                    ).count()
                }
            )

        return Response(data=data, status=status.HTTP_200_OK)
