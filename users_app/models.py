import uuid

# from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Bot_User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tg_id = models.SlugField(unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    tg_full_name = models.CharField(max_length=120)
    tg_username = models.CharField(max_length=120, null=True, blank=True)
    region = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=13)

    # math_score = models.IntegerField(null=True, blank=True)
    # iq_score = models.IntegerField(null=True, blank=True)
    # english_score = models.IntegerField(null=True, blank=True)
    # total_score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0),
    #                                                                      MaxValueValidator(100)])

    create_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_ban = models.BooleanField(default=False)
    is_admin = models.CharField(max_length=2, default="A")
    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-create_time']


class Joylinks_Courses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    info = models.TextField(null=True, blank=True)
    photo = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ____ Kurs Xolati: {self.is_active} __________"


class User_Enroll_Course(models.Model):
    tg_id = models.ForeignKey(Bot_User, on_delete=models.DO_NOTHING)
    course_id = models.ManyToManyField(Joylinks_Courses)
    call_state = models.IntegerField(max_length=1, default=0)
    off_state = models.IntegerField(max_length=1, default=0)

    def __str__(self):
        return f"{self.tg_id} ______ Call State: {self.call_state} ______ O'chirilgan Xolati: {self.off_state}"
