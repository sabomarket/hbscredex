from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models



class Profile (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    address = models.CharField (max_length = 200,  null = True)
    zip_code = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)
    date_of_birth = models.CharField (max_length = 200, null = True)
    home_address = models.CharField (max_length = 200, null = True)
    occupation = models.CharField (max_length = 200, null = True)
    annual_income_range = models.CharField (max_length = 200, null = True)
    pin = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)


    def __str__(self):
        return str(self.name)


class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    main_balance = models.CharField (max_length = 200,  null = True, default = "0",)
    main_income = models.CharField (max_length = 200, null = True, default = "0",)
    main_expense = models.CharField (max_length = 200, null = True, default = "0",)
    crypto_balance = models.CharField (max_length = 200, null = True, default = "0",)
    crypto_income = models.CharField (max_length = 200, null = True,default = "0",)
    crypto_expense = models.CharField (max_length = 200, null = True, default = "0",)
    currency = models.CharField (max_length = 200, null = True, default = "$",)

    def __str__(self):
        return str(self.name)

class Card (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    card_type = models.CharField (max_length = 200,  null = True, default = "0",)
    card_number = models.CharField (max_length = 200, null = True, default = "**** **** **** 2563",)
    exp_date = models.CharField (max_length = 200, null = True, default = "12/24",)
    cvv = models.CharField (max_length = 200, null = True, default = "***",)

    def __str__(self):
        return str(self.name)

class Accountnumber (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    account_number = models.CharField (max_length = 200,  null = True, default = "Generating Account Number...",)


    def __str__(self):
        return str(self.name)

class Order (models.Model):
	STATUS = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	bank = models.CharField(max_length=200, null=True)
	Status = models.CharField(max_length=200, null=True, choices=STATUS)
	account_number = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Withdraw (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    bank = models.CharField (max_length = 200,  null = True, )
    account_number = models.CharField (max_length = 200,  null = True)
    amount = models.CharField (max_length = 200,  null = True)
    status = models.CharField (max_length = 200,  null = True, default = "Pending", )


    def __str__(self):
        return str(self.name)


class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)


class Transfer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    date = models.CharField (max_length = 200)
    name = models.CharField (max_length = 200)
    bank = models.CharField (max_length = 200)
    account_number = models.CharField (max_length = 200)
    amount = models.CharField (max_length = 200)
    charge = models.CharField (max_length = 200)
    type = models.CharField (max_length = 200)
    status = models.CharField (max_length = 200,  null = True, default = "Pending", )


    def __str__(self):
        return str(self.name)

 
