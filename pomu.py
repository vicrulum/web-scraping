from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options  # Suprimir el navegador
# Posicionar en un elemento hover
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd

# Declaramos nuestro web driver
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(
    "C:/Users/victo/AppData/Local/Programs/Python/chromedriver")
wait = WebDriverWait(driver, 10)

# Almacenamos el id de la ventana actual
original_window = driver.current_window_handle

# Ingresamos a la pagina de Servicios en Linea de la UANL
driver.get("https://impomu.com")

for i in range(10000000):
    driver.find_element_by_xpath(
        "//*[@id='im-pomu']").click()
