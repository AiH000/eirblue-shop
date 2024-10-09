from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "author", "genre", "price", "stock", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_author(self):
        author = self.cleaned_data["author"]
        return strip_tags(author)
    
    def clean_genre(self):
        genre = self.cleaned_data["genre"]
        return strip_tags(genre)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)