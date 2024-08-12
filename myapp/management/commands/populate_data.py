from django.core.management.base import BaseCommand
from myapp.models import Categoria, Producto

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            ["1", "Centrum Men X 60 Tabl", "PFIZER PFE", "7702132011819", "Suplemento multivitamínico", "73600", "L01A01", "09/09/2022", "08/09/2024", "Vitaminas"],
            ["2", "Centrum Women X 60 Tabl", "PFIZER PFE", "7702132011857", "Suplemento multivitamínico", "73600", "L01A02", "09/10/2022", "08/10/2024", "Vitaminas"],
            ["3", "Ensoy Adulto Diabeticos Vainilla X 1000 Gr", "LAFRANCOL", "7702870052532", "Suplemento nutricional", "63300", "L01A03", "09/11/2022", "08/11/2024", "Vitaminas"],
            ["4", "Vitybell X 30 Cap", "PROCAPS", "7703153030797", "Suplemento dietario", "112800", "L01A04", "09/12/2022", "08/12/2024", "Vitaminas"],
            ["5", "Dolex Gripa A.C.F. X 12 Tabl", "GLAXO CONSUMER HEALTH CARE", "7451079001543", "Gripe y Resfriado", "15800", "L01A05", "09/09/2022", "08/09/2024", "Analgecicos"],
            ["6", "Noxpirin Plus N.f X 12 Tabl", "LABS SIEGFRIED", "7703234102702", "Gripe y Resfriado", "14100", "L01A06", "09/10/2022", "08/10/2024", "Analgecicos"],
            ["7", "Allegra F. 120 Mg X 10 Tabl", "SANOFI AVENTIS", "7591044008952", "Gripe y Resfriado", "67400", "L01A07", "09/11/2022", "08/11/2024", "Analgecicos"],
            ["8", "Congestex C.F.I. X 10 Cap", "NOVAMED", "7703546031103", "Gripe y Resfriado", "12700", "L01A08", "09/12/2022", "08/12/2024", "Analgecicos"],
            ["9", "Azitromicina 500 Mg X 3 Tabl", "GENFAR", "7702605100491", "Tratamiento para infecciones bacterianas", "11800", "L01A09", "09/09/2022", "08/09/2024", "Antibiotico"],
            ["10", "Levofloxacino 750 Mg X 5 Tabl", "GENFAR", "7702605109616", "Tratamiento de diversas infecciones bacterianas", "46600", "L01A010", "09/10/2022", "08/10/2024", "Antibiotico"],
            ["11", "Cefuroxima 500 Mg X 10 Tabl", "GENFAR", "7702605103935", "Tratamiento de diversas infecciones bacterianas","45300", "L01A011", "09/11/2022", "08/11/2024", "Antibiotico"],
            ["12", "Amoxicilina 500 Mg X 50 Cap", "GENFAR", "7702605100309", "Tratamiento de diversas infecciones bacterianas","32500", "L01A012", "09/12/2022", "08/12/2024", "Antibiotico"],
            ["13", "Valaciclovir 1 Gr Caja X 21 Tabletas", "GENFAR", "7702605109173", "Tratamiento de infecciones por virus", "169500", "L01A013", "09/09/2022", "08/09/2024", "Antivirales"],
            ["14", "Aciclovir 800 Mg X 10 Tabl", "GENFAR", "7702605100132", "Tratamiento de infecciones por virus","19700", "L01A014", "09/10/2022", "08/10/2024", "Antivirales"],
            ["15", "Viroxil 800 Mg Caja X 10 Tabletas", "GIMED SA", "7707341202553", "Tratamiento de infecciones por virus","68500", "L01A015", "09/11/2022", "08/11/2024", "Antivirales"],
            ["16", "Nytax Nitazoxanida 500 Mg X 6 Cap", "PROCAPS", "7703153012410", "Tratamiento de infecciones por virus","90300", "L01A016", "09/12/2022", "08/12/2024", "Antivirales"],           
        ]
        # Referencia de informacion: https://www.tudrogueriavirtual.com/medicina-formulada

        for registro in data:
            codigo = registro[0]
            nombre = registro[1]
            marca = registro[2]
            referencia = registro[3]
            descripcion = registro[4]
            precio = registro[5]
            n_lote = registro[6]
            f_fabricacion = registro[7]
            f_expedicion = registro[8]
            categoria = registro[9]
            
            categoria_obj = Categoria.objects.filter(name=categoria).first()
            if not categoria_obj:
                categoria_obj = Categoria(
                    name=categoria,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.1"
                )
                categoria_obj.save()
                
            producto = Producto.objects.filter(name=nombre).first()
            if not producto:
                producto = Producto(
                    code=codigo,
                    name=nombre,
                    brand=marca,
                    reference=referencia,
                    description=descripcion,
                    price=precio,
                    batch=n_lote,
                    manufacturing=f_fabricacion,
                    expedition=f_expedicion,
                    categoria=categoria_obj,
                    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.2',
                )
                producto.save()
