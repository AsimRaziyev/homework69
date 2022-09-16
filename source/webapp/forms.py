from django import forms
from django.forms import widgets
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "description", "category", "picture"]
        widgets = {
            "description": widgets.Textarea(attrs={"placeholder": "введите текст", "cols": 30, "rows": 3})
        }


class UserReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["description_reviews", "grade"]
        widgets = {
            "description_reviews": widgets.Textarea(attrs={"placeholder": "введите текст", "cols": 30, "rows": 3})
        }
