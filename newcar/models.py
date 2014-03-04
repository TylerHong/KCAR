from django.db import models


class Maker(models.Model):
  mid = models.AutoField(primary_key=True)
  mcode = models.CharField(max_length=2)
  mname = models.CharField(max_length=50)
  def __unicode__(self):
    return self.mname

class Car(models.Model):
  cid = models.AutoField(primary_key=True)
  mid = models.ForeignKey(Maker)
  cname = models.CharField(max_length=50)
  ccode = models.CharField(max_length=3)
  trim = models.CharField(max_length=50)
  def __unicode__(self):
    return self.cname

class Dealer(models.Model):
  did = models.AutoField(primary_key=True)
  cellphone = models.CharField(unique=True, max_length=12)
  email = models.EmailField(unique=True, max_length=50)
  dname = models.CharField(max_length=20)
  passwd = models.CharField(max_length=25)
  mid = models.ForeignKey(Maker)
  branch_name = models.CharField(max_length=20)
  grade = models.CharField(max_length=1)
  memo = models.TextField(blank=True)
  phone = models.CharField(max_length=12, blank=True)
  city = models.CharField(max_length=20)
  address1 = models.CharField(max_length=30)
  address2 = models.CharField(max_length=30, blank=True)
  join_date = models.DateField(auto_now_add=True, editable=False)
  num_send = models.PositiveIntegerField(default=0)
  date_last_send = models.DateField(auto_now_add=False)
  withdraw = models.BooleanField(default=False)
  num_new_sell = models.PositiveIntegerField(default=0)
  reputation = models.FloatField(default=3)
  def __unicode__(self):
    return self.dname

class Buy(models.Model):
  bid = models.AutoField(primary_key=True)
  mid = models.ForeignKey(Maker)
  cid = models.ForeignKey(Car)
  is_lease = models.BooleanField(default=False)
  name = models.CharField(max_length=20)
  cellphone = models.CharField(max_length=12)
  email = models.EmailField(max_length=50)
  passwd = models.CharField(max_length=25)
  detail = models.CharField(max_length=100, blank=True)
  city = models.CharField(max_length=20)
  address1 = models.CharField(max_length=30)
  address2 = models.CharField(max_length=30, blank=True)
  req_date = models.DateTimeField(auto_now_add=True, editable=False)
  is_done = models.BooleanField(default=False)
  is_cancel = models.BooleanField(default=False)
  done_date = models.DateTimeField(blank=True)
  did = models.ForeignKey(Dealer, blank=True)
  satisfaction = models.PositiveIntegerField(default=3)

