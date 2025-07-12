from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from credenciales import USUARIO, CONTRASENIA

# Paso 1: Abrir página
url = "https://www.demoblaze.com/index.html"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# Paso 2: Registro de usuario
registro = driver.find_element(By.ID, "signin2")
registro.click()
time.sleep(3)

usuario_input = driver.find_element(By.ID, "sign-username")
usuario_input.send_keys(USUARIO)

contrasenia_input = driver.find_element(By.ID, "sign-password")
contrasenia_input.send_keys(CONTRASENIA)

boton_registro = driver.find_element(By.XPATH, '//button[text()="Sign up"]')
boton_registro.click()
time.sleep(2)

# Cerrar alerta si aparece
try:
    alerta = driver.switch_to.alert
    alerta.accept()
    print("Registro completado con alerta")
except:
    print("No hubo alerta")

time.sleep(3)

# Paso 3: Login
login = driver.find_element(By.ID, "login2")
login.click()
time.sleep(3)

login_usuario = driver.find_element(By.ID, "loginusername")
login_usuario.send_keys(USUARIO)

login_contra = driver.find_element(By.ID, "loginpassword")
login_contra.send_keys(CONTRASENIA)

login_boton = driver.find_element(By.XPATH, '//button[text()="Log in"]')
login_boton.click()
time.sleep(4)

# Paso 4: Seleccionar dos productos
def agregar_producto(nombre_producto):
    link_producto = driver.find_element(By.LINK_TEXT, nombre_producto)
    link_producto.click()
    time.sleep(2)

    boton_agregar = driver.find_element(By.LINK_TEXT, "Add to cart")
    boton_agregar.click()
    time.sleep(2)

    try:
        alerta = driver.switch_to.alert
        alerta.accept()
    except:
        pass

    driver.back()
    time.sleep(3)

agregar_producto("Samsung galaxy s6")
agregar_producto("Nexus 6")

# Paso 5: Ir al carrito y realizar pedido
carrito = driver.find_element(By.ID, "cartur")
carrito.click()
time.sleep(3)

place_order = driver.find_element(By.XPATH, '//button[text()="Place Order"]')
place_order.click()
time.sleep(2)

# Llenar formulario
driver.find_element(By.ID, "name").send_keys("Gabriel Proaño")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Quito")
driver.find_element(By.ID, "card").send_keys("1234567890123456")
driver.find_element(By.ID, "month").send_keys("07")
driver.find_element(By.ID, "year").send_keys("2025")

driver.find_element(By.XPATH, '//button[text()="Purchase"]').click()
time.sleep(3)

# Confirmar
driver.find_element(By.XPATH, '//button[text()="OK"]').click()
time.sleep(2)

# Paso 6: Logout
logout = driver.find_element(By.ID, "logout2")
logout.click()

# Fin
driver.quit()
