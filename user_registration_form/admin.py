# # user_registration_form/admin.py

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
# from django.utils.html import format_html


# class CustomUserAdmin(UserAdmin):

#     list_display = (
#         "username",
#         "email",
#         "mobile_number",
#         "hobby",
#         "country",
#         "profile_pic_thumb",
#         "is_staff",
#         "is_active",
#     )

#     list_filter = ("is_staff", "is_active", "country")

#     fieldsets = (
#         (None, {"fields": ("username", "email", "password")}),
#         (
#             "Personal info",
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "mobile_number",
#                     "hobby",
#                     "country",
#                     "profile_pic",
#                 )
#             },
#         ),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )

#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "username",
#                     "email",
#                     "password1",
#                     "password2",
#                     "mobile_number",
#                     "hobby",
#                     "country",
#                     "profile_pic",
#                     "is_staff",
#                     "is_active",
#                 ),
#             },
#         ),
#     )

#     search_fields = ("username", "email", "mobile_number", "hobby", "country")
#     ordering = ("username",)
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )

#     def profile_pic_thumb(self, obj):
#         if obj.profile_pic:
#             return format_html(
#                 '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
#                 obj.profile_pic.url,
#             )
#         return "-"

#     profile_pic_thumb.short_description = "Profile Pic"


# admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from user_registration_form.models import CustomUser, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    readonly_fields = ("profile_pic_thumb",)

    def profile_pic_thumb(self, obj):
        if obj.profile_pic:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
                obj.profile_pic.url,
            )
        return "-"

    profile_pic_thumb.short_description = "Profile Pic"


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

    list_display = (
        "username",
        "email",
        "get_mobile",
        "get_hobby",
        "get_country",
        "get_profile_pic",
        "is_staff",
        "is_active",
    )

    def get_mobile(self, obj):
        return obj.profile.mobile_number if hasattr(obj, "profile") else "-"

    get_mobile.short_description = "Mobile"

    def get_hobby(self, obj):
        return obj.profile.hobby if hasattr(obj, "profile") else "-"

    get_hobby.short_description = "Hobby"

    def get_country(self, obj):
        return obj.profile.country if hasattr(obj, "profile") else "-"

    get_country.short_description = "Country"

    def get_profile_pic(self, obj):
        if hasattr(obj, "profile") and obj.profile.profile_pic:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
                obj.profile.profile_pic.url,
            )
        return "-"

    get_profile_pic.short_description = "Profile Pic"


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
