# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from math import ceil



class CustomUser(AbstractUser):
    def __str__(self):

        return self.name +" "+ self.password +" "+ self.email


# GRADE_OPTIONS
GRADE_OPTIONS = (
('HIGH_SCHOOL', 'High School'),
('UNDERGRADUATE','Undergraduate'),
('MASTERS', 'Masters'),
('DOCTORATE', 'Doctorate')
)

# #TIME Options
# TIME_OPTIONS=(
# (6, '6 Hours'),
# (12, '12 Hours'),
# (1, '1 Day'),
# (2, '2 Days'),
# (3, '3 Days'),
# (4, '4 Days'),
# (5, '5 Days'),
# (7, '7 Days'),
# (14, '14 Days'),
# (30, '30 Days'),
#
# )

class Order(models.Model):
    grade = models.CharField(choices=GRADE_OPTIONS)
    words = models.IntegerField(min_value=275, max_value=5500)
    duration = models.IntegerField(min_value=1, max_value=30, options=TIME_OPTIONS)

    def map_words_to_pages():
        #insert the conversion rate here
        words_per_page = 275
        return ceil(self.words / words_per_page)
