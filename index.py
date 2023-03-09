from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # Suprimir el navegador
# Posicionar en un elemento hover
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd

# Declaramos nuestro web driver
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(
    "C:/Users/victo/AppData/Local/Programs/Python/Python39/chromedriver", options=op)
wait = WebDriverWait(driver, 10)

# Almacenamos el id de la ventana actual
original_window = driver.current_window_handle

# Ingresamos a la pagina de Servicios en Linea de la UANL
driver.get("https://www.uanl.mx/enlinea/")
print(driver.title)

# Tenemos que especificar que ingresaremos dentro de un marco o etiqueta <iframe/>
frame_0 = driver.find_element_by_name('loginbox')
driver.switch_to.frame(frame_0)

# Ingresamos los datos de cuenta y contraseña
user = driver.find_element_by_id("cuenta")
user.send_keys("askdhkasjhd")

user = driver.find_element_by_id("pass")
user.send_keys("asmdmsanb")

# Seleccionamo el boton de ingresar
driver.find_element_by_xpath(
    "/html/body/div/form/fieldset/div[4]/button").click()

# Nos posicionamos en el boton de Nexus
nexus = driver.find_element_by_xpath(
    "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[3]/td/a/img")
webdriver.ActionChains(driver).move_to_element(nexus).perform()

# Seleccionamos el boton de ingresar a Nexus
info = driver.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td[2]/div[4]/table/tbody/tr[2]/td[2]/div/div/form')
print(info)

# Esperamos hasta que se cree una nueva ventana o tab
wait.until(EC.number_of_windows_to_be(2))

# Se hace un ciclo for para encontrar un nuevo manejo de ventana
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Esperamos hasta que la ventana termine de cargar
wait.until(EC.title_is("Nexus7"))

driver.implicitly_wait(10)

driver.find_element_by_xpath(
    "/html/body/app-root/app-appmain/div/mat-sidenav-container/mat-sidenav[1]/div/mat-nav-list/a[4]/div/i").click()
print("end")
