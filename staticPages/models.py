"""
Models for the staticPages app.

This module contains the data models for the staticPages app,
including the Collection and Piece models.
"""

from django.db import models

class Collection(models.Model):
    """
    Model representing a jewelry collection.
    """
    collection_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self): #to let the name of collection appear (e.g about us),this functionis written
        return str(self.collection_name)


class Piece(models.Model):
    """
    Model representing a piece of jewelry within a collection.
    """
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)
