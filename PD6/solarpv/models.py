from django.db import models

class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=30)
    clientType = models.CharField(max_length=30)

class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    jobTitle = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    officePhone = models.CharField(max_length=30)
    cellPhone = models.CharField(max_length=30)
    prefix = models.CharField(max_length=30)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)

class TestStandard(models.Model):
    standardID = models.AutoField(primary_key=True)
    standardName = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    publishedDate = models.DateField()

class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postalCode = models.IntegerField()
    country = models.CharField(max_length=30)
    phoneNumber = models.IntegerField()
    faxNumber = models.IntegerField()
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)

class Product(models.Model):
    modelNumber = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=30)
    cellTechnology = models.CharField(max_length=30)
    cellManufacturer = models.CharField(max_length=30)
    numberOfCells = models.IntegerField()
    numberOfCellsInSeries = models.IntegerField()
    numberOfSeriesInString = models.IntegerField()
    numberOfDiodes = models.IntegerField()
    productLength = models.IntegerField()
    productWidth = models.IntegerField()
    productWeight = models.IntegerField()
    superstateType = models.CharField(max_length=30)
    superstateManufacturer = models.CharField(max_length=30)
    frameType = models.CharField(max_length=30)
    frameAdhesive = models.CharField(max_length=30)
    encapsulateType = models.CharField(max_length=30)
    encapsulantManufacturer = models.CharField(max_length=30)
    junctionBoxType = models.CharField(max_length=30)
    junctionBoxManufacturer = models.CharField(max_length=30)

class Certificate(models.Model):
    certificateNumber = models.AutoField(primary_key=True)
    certID = models.IntegerField()
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    reportNumber = models.IntegerField()
    issueDate = models.DateField()
    standardID = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelNumber = models.ForeignKey(Product, on_delete=models.CASCADE)

class TestSequence(models.Model):
    sequenceID = models.AutoField(primary_key=True)
    sequenceName = models.CharField(max_length=30)

class PerformanceData(models.Model):
    modelNumber = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequenceID = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    maxSystemVoltage = models.IntegerField()
    voc = models.IntegerField()
    isc = models.IntegerField()
    vmp = models.IntegerField()
    imp = models.IntegerField()
    pmp = models.IntegerField()
    ff = models.IntegerField()

class Service(models.Model):
    serviceID = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    isFIRequired = models.CharField(max_length=30)
    fIFrequency = models.IntegerField()
    standardID = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
