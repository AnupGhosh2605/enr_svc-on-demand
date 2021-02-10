# Generated by Django 2.1.15 on 2021-02-10 05:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('UserFirstName', models.CharField(max_length=100)),
                ('UserMiddleName', models.CharField(max_length=100)),
                ('UserLastName', models.CharField(max_length=100)),
                ('UserEmail', models.CharField(max_length=100, unique=True)),
                ('ContactCell', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppliationList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApplicationName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AssetsDetailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FileName', models.CharField(default=None, max_length=1000, null=True)),
                ('FileExtension', models.CharField(default=None, max_length=50, null=True)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=300)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='City_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForceCloseCategoryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ForceCloseCategoryName', models.CharField(max_length=300)),
                ('DefaultValue', models.CharField(max_length=300)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Force_Close_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LanguageName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NotificationDate', models.DateField(auto_now_add=True)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('AssetsDetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.AssetsDetailList')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CategoryList')),
                ('City', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CityList')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseTypeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResponseType', models.CharField(max_length=100)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Response_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReviewDate', models.DateField(auto_now_add=True)),
                ('ReviewNote', models.CharField(max_length=3999)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('IsAdminApproved', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('AssetsDetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.AssetsDetailList')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CategoryList')),
                ('City', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CityList')),
                ('FromUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review_From_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubCategoryName', models.CharField(max_length=300)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CategoryList')),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCat_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionDetailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriptionItemItem', models.CharField(max_length=300)),
                ('ConfiguredValue', models.CharField(max_length=300)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_Details_Updated_By', to=settings.AUTH_USER_MODEL)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_Details_Subscriber', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriptionItemName', models.CharField(max_length=300)),
                ('DefaultValue', models.CharField(max_length=300)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_Item_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriptionName', models.CharField(max_length=300)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateTypeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SMSTemplateType', models.CharField(max_length=300)),
                ('WhatsAppTemplateType', models.CharField(max_length=1000)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Template_Updated_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopicDetailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicDate', models.DateField(auto_now_add=True)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('AssetsDetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.AssetsDetailList')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CategoryList')),
                ('City', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CityList')),
                ('SubCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubCategoryList')),
            ],
        ),
        migrations.CreateModel(
            name='TopicList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicName', models.CharField(max_length=300)),
                ('TopicDate', models.DateField(auto_now_add=True)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('IsClose', models.BooleanField(default=True)),
                ('CloseDate', models.DateField(auto_now_add=True)),
                ('ForceCloseReason', models.CharField(max_length=3999)),
                ('IsNotification', models.BooleanField(default=True)),
                ('SMSText', models.CharField(max_length=150)),
                ('WhatsAppText', models.CharField(max_length=1000)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CategoryList')),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CityList')),
                ('CloseBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Topic_Closed_By', to=settings.AUTH_USER_MODEL)),
                ('ForceCloseCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.ForceCloseCategoryList')),
                ('SubCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.SubCategoryList')),
                ('UpdatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Topic_Updated_By', to=settings.AUTH_USER_MODEL)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Topic_Subscriber', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserType', models.CharField(max_length=100)),
                ('UpdatedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='topicdetaillist',
            name='Topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.TopicList'),
        ),
        migrations.AddField(
            model_name='topicdetaillist',
            name='UpdatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Topic_details_Updated_By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topicdetaillist',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Topic_details_Subscriber', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewlist',
            name='SubCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubCategoryList'),
        ),
        migrations.AddField(
            model_name='reviewlist',
            name='ToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review_To_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewlist',
            name='Topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.TopicList'),
        ),
        migrations.AddField(
            model_name='reviewlist',
            name='UpdatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Review_Updated_By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewlist',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review_Subscriber', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notificationlist',
            name='SubCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubCategoryList'),
        ),
        migrations.AddField(
            model_name='notificationlist',
            name='ToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notification_To_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notificationlist',
            name='Topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.TopicList'),
        ),
        migrations.AddField(
            model_name='notificationlist',
            name='UpdatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notification_Updated_By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notificationlist',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notification_Subscriber', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assetsdetaillist',
            name='Topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.TopicList'),
        ),
        migrations.AddField(
            model_name='assetsdetaillist',
            name='UpdatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assets_Updated_By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appliationlist',
            name='Language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.LanguageList'),
        ),
        migrations.AddField(
            model_name='userlist',
            name='Application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AppliationList'),
        ),
        migrations.AddField(
            model_name='userlist',
            name='UserType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserType'),
        ),
        migrations.AddField(
            model_name='userlist',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userlist',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
