from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from credenciales import USUARIO, CONTRASENIA

# Abrir página
url = "https://www.demoblaze.com/index.html"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# Registro de usuario
registro = driver.find_element(By.ID, '//*[@id="signin2"]')
registro.click()
time.sleep(3)

usuario_input = driver.find_element(By.ID, '//*[@id="sign-username"]')
usuario_input.send_keys(USUARIO)

contrasenia_input = driver.find_element(By.ID, '//*[@id="sign-password"]')
contrasenia_input.send_keys(CONTRASENIA)

boton_registro = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
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

#  Login
login = driver.find_element(By.ID, '//*[@id="login2"]')
login.click()
time.sleep(3)

login_usuario = driver.find_element(By.ID, '//*[@id="loginusername"]')
login_usuario.send_keys(USUARIO)

login_contra = driver.find_element(By.ID, '//*[@id="loginpassword"]')
login_contra.send_keys(CONTRASENIA)

login_boton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_boton.click()
time.sleep(4)

#  Seleccionar dos productos
def agregar_producto(nombre_producto):
    link_producto = driver.find_element(By.LINK_TEXT, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
    link_producto.click()
    time.sleep(2)

    boton_agregar = driver.find_element(By.LINK_TEXT, '//*[@id="tbodyid"]/div[2]/div/a')
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

# Ir al carrito y realizar pedido
carrito = driver.find_element(By.ID, '//*[@id="cartur"]/font/font')
carrito.click()
time.sleep(3)

place_order = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
place_order.click()
time.sleep(2)

# Llenar formulario
driver.find_element(By.ID, "name").send_keys("Gabriel Proaño")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Quito")
driver.find_element(By.ID, "card").send_keys("1234567890123456")
driver.find_element(By.ID, "month").send_keys("07")
driver.find_element(By.ID, "year").send_keys("2025")

driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
time.sleep(3)

# Confirmar
driver.find_element(By.XPATH, '/html/body/div[11]/div[7]/div/button').click()
time.sleep(2)

#  Logout
logout = driver.find_element(By.ID, '//*[@id="logout2"]')
logout.click()

#Final
driver.quit()
