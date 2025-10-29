from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory(login_in_driver):
    try:
        #Validacion titulo
        driver = login_in_driver
        assert driver.title == "Swag Labs"

        #Validacion de existencia de productos
        products  = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"

        #Validacion de menu y filtro
        wait = WebDriverWait(driver, 10)
        menu = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
        print("El menú de navegación fue encontrado y es visible.")
        filtro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
        print("El filtro fue encontrado y es visible.")


    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()


        