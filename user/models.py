from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
choose=[
    ("ABUJA","ABUJA"),
    ("ABIA","ABIA"),("ADAMAWA","ADAMAWA"),("AKWAIBOM","AKWAIBOM"),("ANAMBRA","ANAMBRA"),("BAUCHI","BAUCHI"),
    ("BAYELSA","BAYELSA"),("BENUE","BENUE"),("BORNU","BORNU"),("CROSSRIVER","CROSSRIVER"),("DELTA","DELTA"),
    ("EBONYI","EBONYI"),("EDO","EDO"),("EKITI","EKITI"),("ENUGU","ENUGU"),("GOMBE","GOMBE"),
    ("IMO","IMO"),("JIGAWA","JIGAWA"),("KADUNA","KADUNA"),("KANO","KANO"),("KASTINA","KASTINA"),
    ("KEBI","KEBI"),("KOGI","KOGI"),("KWARA","KWARA"),("LAGOS","LAGOS"),("NASSARAWA","NASSARAWA"),
    ("NIGER","NIGER"),("OGUN","OGUN"),("ONDO","ONDO"),("OSUN","OSUN"),("OYO","OYO"),("PLATEAU","PLATEAU"),
    ("RIVERS","RIVERS"),("SOKOTO","SOKOTO"),("TARABA","TARABA"),("YOBE","YOBE"),("ZAMFARA","ZAMFARA")

]

notification=[
    ("Your order has been taken and is being processed.","Your order has been taken and is being processed."),
    ("Your order has been delivered!","Your order has been delivered!"),
    ("You have paid 500 registration fee.","You have paid 500 registration fee."),
    ("Your product upload was not approved. Please contact the company surpport line.","Your product upload was not approved. Please contact the company surpport line."),
    ("Your product upload has been approved!","Your product upload has been approved!")
]

class Vendor(models.Model):
    bussiness_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="profile_pics",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bussiness_address=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    Cac=models.IntegerField()
    nearest_landmark=models.CharField(max_length=100)
    state=models.CharField(max_length=100, choices=choose)
    lga=models.CharField(max_length=100,null=True)


    def __str__(self):

        return self.bussiness_name
    


class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    notification=models.CharField(max_length=1000,choices=notification)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):

        return self.notification


    




