from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']

     def clean_category(self):
       category = self.cleaned_data.get('category')
       if not category:
         raise forms.ValidationError('This Field is Required')
         return category

     

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name']

