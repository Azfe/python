# from setuptools import setup

# setup(
#     name="paquete_calculos",
#     version="1.0",
#     description="Paquete de redondeo y potencia",
#     author="Alex",
#     author_email="alexzapata1984@gmail.com",
#     url="azup.es",
#     packages=["calculos", "calculos.redondeo_potencia"]   
# )

from setuptools import setup, find_packages

setup(
    name="paquete_calculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Alex",
    author_email="alexzapata1984@gmail.com",
    url="azup.es",
    packages=find_packages()  
)