from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname + " " + self.lastname


"""
create table member(
id int not null,
firstname varchar(255) not null,
lastname varchar(255) not null
primary key(id)
);
"""
class Img(models.Model):
    image = models.ImageField(upload_to='products',default=None)

    def __str__(self):
        return self.image