from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver_path = r'/snap/bin/firefox.geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

driver.get("https://oauth.upeu.edu.pe/accounts/login/?next=/oauth/authorize/%3Fresponse_type%3Dtoken%26client_id%3DbAjEWz6QgPe06WJVMOEqEvBOQc5Wvn8G63w11nfs%26redirect_uri%3Dhttps%253A%252F%252Flamb-academic.upeu.edu.pe%252Fcallback%26scope%3Dread%2520introspection")
#login
driver.find_element(by=By.XPATH, value="//input[@id='id_username']").send_keys("marioccallo")
driver.find_element(by=By.XPATH, value="//input[@id='id_password']").send_keys("Moscasmolestan1")
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

#