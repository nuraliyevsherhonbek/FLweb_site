from django.db import models


class Course(models.Model):
    image = models.ImageField(upload_to='course_images/', null=True)
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    cost = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Application(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='applications', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.first_name,} {self.last_name}"


class Result(models.Model):
    student_name = models.CharField(max_length=300)
    results_image = models.ImageField(upload_to='results/')
    description = models.CharField(max_length=500)
    score = models.CharField(max_length=30)
    university_or_ielts = models.CharField(max_length=500, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.student_name} | {self.score} | {self.university_or_ielts}"


class SocialNetwork(models.Model):
    name = models.CharField(max_length=50,unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class StudentNumber(models.Model):
    number = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Studentlar soni'



