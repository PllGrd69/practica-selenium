from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver_path = r'/snap/bin/firefox.geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element("name", "name").send_keys("Mario")
driver.find_element("name", "email").send_keys("mario@upeu.edu.pe")
elementcss = driver.find_element(By.ID, "exampleCheck1").click()
elementcss = driver.find_element(By.ID, "exampleInputPassword1").send_keys("contrasena")

driver.find_element(by=By.XPATH, value="//input[@id='id_username']").click()
driver.find_element(by=By.XPATH, value="//input[@name='bday']").send_keys("2001-12-12")


elementcss = driver.find_element(By.ID, "inlineRadio1").click()

driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

#select = Select(driver.find_element_by_id('fruits01'))
#elementcss = driver.find_element(By.ID, "exampleFormControlSelect1").select.select_by_visible_text('Female')












