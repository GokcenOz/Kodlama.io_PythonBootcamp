from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com/")
sleep(3)

logInButton=driver.find_element(By.ID,"login-button")
logInButton.click()
sleep(4)
errorText=driver.find_element(By.XPATH,"//h3[text()='Epic sadface: Username is required']").text

print(f"1.test sonucu: {errorText}")

sleep(5)

