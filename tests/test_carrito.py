from selenium.webdriver.common.by import By
from selenium import webdriver

def test_carrito(login_in_driver):
    try:
        #Añadir un producto al carrito
        driver = login_in_driver
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        productos[0].find_element(By.TAG_NAME, "button").click()

        #Validacion contador carrito    
        carrito_texto = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito_texto == "1"
        print("Carrito OK", carrito_texto)

        #Entrar al carrito y validar que se carguen productos
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        productos_agregados  = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos_agregados) > 0, "No hay productos visibles en la pagina"

    except Exception as e:
        print(f"Error en test_carrito: {e}")
        raise

    finally:
        driver.quit()