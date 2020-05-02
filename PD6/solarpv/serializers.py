from rest_framework import serializers
from .models import Product
from .models import Certificate
from .models import Service

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('modelNumber','productName','cellTechnology','cellManufacturer','numberOfCells','numberOfCellsInSeries','numberOfSeriesInString','numberOfDiodes',
            'productLength','productWidth','productWeight','superstateType','superstateManufacturer','frameType','frameAdhesive','encapsulateType','encapsulantManufacturer',
            'junctionBoxType','junctionBoxManufacturer')

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('certificateNumber','certID','userID','reportNumber','issueDate','standardID','locationID','modelNumber')

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('serviceID','serviceName','description','isFIRequired','fIFrequency','standardID')
