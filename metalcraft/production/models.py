from django.db import models

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    raw_materials = models.ManyToManyField(RawMaterial, through='ProductRawMaterial')
    workstations = models.ManyToManyField('WorkStation', through='ProductWorkStation')
    
    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Order for {self.product.name}"

class WorkStation(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ProductionStage(models.Model):
    name = models.CharField(max_length=100)
    sequence = models.IntegerField()
    workstation = models.ForeignKey(WorkStation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class ProductRawMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity_used = models.IntegerField()

class ProductWorkStation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    workstation = models.ForeignKey(WorkStation, on_delete=models.CASCADE)
    stage = models.ForeignKey(ProductionStage, on_delete=models.CASCADE)
