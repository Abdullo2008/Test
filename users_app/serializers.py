from rest_framework.serializers import ModelSerializer

from .models import Bot_User


class UserSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = "__all__"


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['is_admin']


class UserBanSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['is_ban']


class UserActiveSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['is_active']


class PersonalDataSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['first_name', 'last_name', 'region', 'district', 'phone_number']


class UpdateFirstNameSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['first_name']


class UpdateLastNameSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['last_name']


class UpdateRegionSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['region']


class UpdateDistrictSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['district']


class UpdatePhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['phone_number']

class UpdateAdminSerializer(ModelSerializer):
    class Meta:
        model = Bot_User
        fields = ['is_admin']

# class ScoresSerializer(ModelSerializer):
#     class Meta:
#         model = Bot_User
#         fields = ['math_score', 'iq_score', 'english_score', 'total_score']


# class OlimpiadaSerializer(ModelSerializer):
#     class Meta:
#         model = Bot_User
#         fields = ['olimpiada']


# class ExcelSerializers(ModelSerializer):
#     class Meta:
#         model = Bot_User
#         fields = ['tg_id', 'is_active', 'first_name', 'last_name', 'tg_full_name', 'tg_username', 'region', 'district',
#                   'phone_number', 'create_time']


# class ExcelGrandSerializers(ModelSerializer):
#     class Meta:
#         model = Bot_User
#         fields = ['tg_id', 'is_active', 'first_name', 'last_name', 'tg_full_name', 'tg_username', 'region', 'district',
#                   'phone_number', 'create_time']
