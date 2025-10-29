El proposito de este proyecto es poner en practica todo lo aprendido hasta el momento en el curso, usando la pagina https://www.saucedemo.com/ para interactuar y automatizar tests.

Las herramientas utilizas fueron Python, Selenium WebDriver y Pytest. Ademas, se uso Git y GitHub para cargar el proyecto.

Se instalaron 2 frameworks en la terminal para poder trabajar, Pytest y Selenium. 
Los codigos a ejecutar en la terminal para que las pruebas funcionen son:
- pip install pytest
- pip install selenium
Luego, dentro de cada archivo, se importaron las siguientes librerias:

import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Para ejecutar las pruebas, hay que correr el archivo "run_tests.py". Va a hacerse un testeo de todas las pruebas y a la vez generar un reporte en html.