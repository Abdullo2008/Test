from django.contrib import admin


from .models import Bot_User, Joylinks_Courses, User_Enroll_Course


# from django import forms


@admin.register(Bot_User)
class JoyLinkUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'is_admin', 'is_active', 'is_ban', 'tg_id']
    ordering = ['-create_time']
    list_editable = ['is_admin', 'is_ban', "is_active"]
    search_help_text = "Foydalanuvchilarni ism, familiya yoki Telegram foydalanuvchi nomi bo'yicha qidiring."
    search_fields = ['tg_id', 'is_admin', 'first_name', 'last_name']
    list_filter = ['create_time']
    list_per_page = 100
    list_max_show_all = 500
    # save_as = True
    # show_facets = ShowFacets.ALLOW
    # inlines = [Bot_User]


admin.site.register(Joylinks_Courses)
# class JoyLinkUserAdmin(admin.ModelAdmin):
#     pass


admin.site.register(User_Enroll_Course)
# class JoyLinkUserAdmin(admin.ModelAdmin):
#     pass
