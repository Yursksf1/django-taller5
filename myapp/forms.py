from django.forms import ModelForm
from myapp.models import Producto

# Create the form class.
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            "code",
            "name",
            "brand",
            "reference",
            "description",
            "price",
            "batch",
            "manufacturing",
            "expedition",
            "categoria",
        ]