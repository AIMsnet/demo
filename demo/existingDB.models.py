# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DatatableStudents(models.Model):
    sname = models.CharField(max_length=125)
    smob = models.CharField(max_length=10)
    saddress = models.CharField(max_length=225)
    pin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'datatable_students'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoFormsClient(models.Model):
    cname = models.CharField(max_length=100)
    cmobno = models.CharField(max_length=10)
    address = models.CharField(max_length=125)
    pincode = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'django_forms_client'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FilterdataEmployee(models.Model):
    ename = models.CharField(max_length=225)
    emob = models.CharField(max_length=10)
    eadd = models.CharField(max_length=225)
    pin = models.CharField(max_length=6)
    edept = models.CharField(max_length=125)

    class Meta:
        managed = False
        db_table = 'filterdata_employee'


class OrmAccount(models.Model):
    atype = models.CharField(max_length=100)
    accno = models.CharField(db_column='accNo', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orm_account'


class OrmAuthor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'orm_author'


class OrmBankdetails(models.Model):
    balance = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'orm_bankdetails'


class OrmBankdetailsAccount(models.Model):
    bankdetails = models.ForeignKey(OrmBankdetails, models.DO_NOTHING)
    account = models.ForeignKey(OrmAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orm_bankdetails_account'
        unique_together = (('bankdetails', 'account'),)


class OrmBankdetailsCustomer(models.Model):
    bankdetails = models.ForeignKey(OrmBankdetails, models.DO_NOTHING)
    customer = models.ForeignKey('OrmCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orm_bankdetails_customer'
        unique_together = (('bankdetails', 'customer'),)


class OrmBook(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'orm_book'


class OrmBookAuthor(models.Model):
    book = models.ForeignKey(OrmBook, models.DO_NOTHING)
    author = models.ForeignKey(OrmAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orm_book_author'
        unique_together = (('book', 'author'),)


class OrmCustomer(models.Model):
    name = models.CharField(max_length=100)
    mobno = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'orm_customer'


class OrmDiscovry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    scientist = models.ForeignKey('OrmScientist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orm_discovry'


class OrmScientist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'orm_scientist'


class Test(models.Model):
    tconst = models.CharField(max_length=45, blank=True, null=True)
    titletype = models.CharField(db_column='titleType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    primarytitle = models.CharField(db_column='primaryTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    originaltitle = models.CharField(db_column='originalTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isadult = models.CharField(db_column='isAdult', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startyear = models.CharField(db_column='startYear', max_length=45, blank=True, null=True)  # Field name made lowercase.
    endyear = models.CharField(db_column='endYear', max_length=45, blank=True, null=True)  # Field name made lowercase.
    runtimeminutes = models.CharField(db_column='runtimeMinutes', max_length=45, blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
