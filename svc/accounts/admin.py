from django.contrib import admin
from .models import (
    LanguageList,
    AppliationList,
    UserType,
    UserList,
    CityList,
    CountryList,
    ResponseTypeList,
    TemplateTypeList,
    CategoryList,
    SubCategoryList,
    SubscriptionList,
    SubscriptionItemList,
    ForceCloseCategoryList,
    SubscriptionDetailList,
    TopicList,
    AssetsDetailList,
    TopicDetailList,
    NotificationList,
    ReviewList,
    CategoryInCity
)
# Register your models here.

admin.site.register(CategoryInCity)
admin.site.register(LanguageList)
admin.site.register(AppliationList)
admin.site.register(UserType)
admin.site.register(UserList)
admin.site.register(CityList)
admin.site.register(ResponseTypeList)
admin.site.register(CountryList)
admin.site.register(TemplateTypeList)
admin.site.register(CategoryList)
admin.site.register(SubCategoryList)
admin.site.register(SubscriptionList)
admin.site.register(SubscriptionItemList)
admin.site.register(ForceCloseCategoryList)
admin.site.register(SubscriptionDetailList)
admin.site.register(TopicList)
admin.site.register(AssetsDetailList)
admin.site.register(TopicDetailList)
admin.site.register(NotificationList)
admin.site.register(ReviewList)
