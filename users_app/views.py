from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# @api_view(['GET'])
# def ExcelGrandUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, total_score__gte=60)
#         serializer = ExcelGrandSerializers(snippets, many=True)
#         return Response(serializer.data)


@api_view(['GET', 'POST'])
def UserList(request):
    if request.method == 'GET':
        snippets = Bot_User.objects.filter(is_active=True)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def NoOlimpiadaUserList(request):
    if request.method == 'GET':
        snippets = Bot_User.objects.filter(is_active=True, olimpiada=False)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def ExcelOlimpiadaUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, olimpiada=True)
#         serializer = ExcelSerializers(snippets, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def ExcelNoOlimpiadaUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, olimpiada=False)
#         serializer = ExcelSerializers(snippets, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def OlimpiadaUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, olimpiada=True)
#         serializer = UserSerializer(snippets, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def TopSoreUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, total_score__gte=60).order_by('-total_score',
#                                                                                          '-create_time')[
#                    :10]
#         serializer = UserSerializer(snippets, many=True)
#         ser_data = serializer.data
#         if len(ser_data) <= 9:
#             ser_data = []
#         return Response(ser_data)

#
# @api_view(['GET'])
# def NextTopSoreUserList(request):
#     if request.method == 'GET':
#         snippets = Bot_User.objects.filter(is_active=True, total_score__gte=60).order_by('-total_score',
#                                                                                          '-create_time')[
#                    :20]
#         serializer = UserSerializer(snippets, many=True)
#         ser_data = serializer.data[10:20]
#         if len(ser_data) <= 9:
#             ser_data = []
#         return Response(ser_data)


@api_view(['GET', 'PUT', 'DELETE'])
def UserDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def ScoreList(request):
#     if request.method == 'GET':
#         snippets = User.objects.filter(is_active=True)
#         serializer = ScoresSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ScoresSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def ScoreDetail(request, telegram_id):
#     try:
#         user = get_object_or_404(User, telegram_id=telegram_id, is_active=True)
#     except User.DoesNotExist:
#         return Response(None, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ScoresSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ScoresSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def PermissionDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PermissionSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PermissionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def UserBanDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserBanSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserBanSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def UserActiveDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserActiveSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserActiveSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def PersonalDataDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalDataSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonalDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def FirstNameDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateFirstNameSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateFirstNameSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def LastNameDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateLastNameSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateLastNameSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def RegionDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateRegionSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateRegionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def DistrictDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateDistrictSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateDistrictSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def PhoneNumberDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdatePhoneNumberSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdatePhoneNumberSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT'])
# def OlimpiadaDetail(request, telegram_id):
#     try:
#         user = get_object_or_404(User, telegram_id=telegram_id, is_active=True)
#     except User.DoesNotExist:
#         return Response(None, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = OlimpiadaSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = OlimpiadaSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def UserCountList(request):
    if request.method == 'GET':
        snippets = Bot_User.objects.filter(is_active=True)
        serializer = UserSerializer(snippets, many=True)
        ser_data = serializer.data
        ser_data = len(ser_data)
        return Response(ser_data)


@api_view(['GET', 'POST'])
def AdminCountList(request):
    if request.method == 'GET':
        snippets = Bot_User.objects.filter(is_active=True)
        serializer = UserSerializer(snippets, many=True)
        ser_data = serializer.data
        ser_data = len(ser_data)
        return Response(ser_data)

    elif request.method == 'POST':
        snippets = Bot_User.objects.filter(is_active=True, is_admin=request.data['is_admin'])
        serializer = UserSerializer(snippets, many=True)
        return Response({"count": len(serializer.data),
                         "data": serializer.data})


@api_view(['GET', 'PUT'])
def AdminDetail(request, tg_id):
    try:
        user = get_object_or_404(Bot_User, tg_id=tg_id, is_active=True)
    except Bot_User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateAdminSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateAdminSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
