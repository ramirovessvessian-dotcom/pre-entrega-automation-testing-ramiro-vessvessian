from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
import utils

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise

    finally:
        driver.quit()