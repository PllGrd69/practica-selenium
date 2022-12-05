from selenium import webdriver

#driver_path = r'/snap/bin/firefox.geckodriver'
#driver = webdriver.Firefox(executable_path=driver_path)
driver_path = r'/home/estudiante/Descargas/edgedriver_linux64/msedgedriver'
driver = webdriver.Edge(executable_path=driver_path)


driver.maximize_window()

driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.minimize_window()
driver.back()
driver.refresh()

driver.close()