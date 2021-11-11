from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


JOB_TITLE = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    # location = ""
    job_type = models.CharField(max_length=15, choices=JOB_TITLE)
    description = models.TextField(max_length=1000, default='')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    image = models.ImageField(upload_to='job/',default='')

    def __str__(self):
        return self.title


