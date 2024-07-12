from django.urls import path, register_converter

from .views import DistrictDetail, PhoneNumberDetail, AdminCountList, AdminDetail
from .views import UserBanDetail, UserActiveDetail, PersonalDataDetail, FirstNameDetail, LastNameDetail, RegionDetail
from .views import UserCountList, UserList, UserDetail, PermissionDetail


class TelegramIDConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(TelegramIDConverter, 'tg_id')

urlpatterns = [
    path('users/', UserList),
    path('count-users/', UserCountList),
    # path('excel-olimpiada-users/', ExcelOlimpiadaUserList),
    # path('excel-no-olimpiada-users/', ExcelNoOlimpiadaUserList),
    # path('excel-grand-users/', ExcelGrandUserList),
    # path('olimpiada-users/', OlimpiadaUserList),
    # path('no-olimpiada-users/', NoOlimpiadaUserList),
    # path('top-users/', TopSoreUserList),
    # path('next-top-users/', NextTopSoreUserList),
    path('users/<tg_id:tg_id>/', UserDetail),
    # path('users/<tg_id:tg_id>/olimpiada/', OlimpiadaDetail),
    # path('users/<tg_id:tg_id>/scores/', ScoreDetail),
    path('users/<tg_id:tg_id>/permissions/', PermissionDetail),
    path('users/<tg_id:tg_id>/ban/', UserBanDetail),
    path('users/<tg_id:tg_id>/active/', UserActiveDetail),
    path('users/<tg_id:tg_id>/personal-data/', PersonalDataDetail),
    path('users/<tg_id:tg_id>/first-name/', FirstNameDetail),
    path('users/<tg_id:tg_id>/last-name/', LastNameDetail),
    path('users/<tg_id:tg_id>/region/', RegionDetail),
    path('users/<tg_id:tg_id>/district/', DistrictDetail),
    path('users/<tg_id:tg_id>/phone-number/', PhoneNumberDetail),
    path('admins/', AdminCountList),
    path('admins/<tg_id:tg_id>/is-admin/', AdminDetail),
]
