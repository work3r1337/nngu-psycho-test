import time, random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


print("Введите логин: ")
login = input()
print("Введите пароль: ")
password = input()
gender = "female"
print("Ваш пол женский?(y/n)")
if input() == 'n':
    gender = "male"
print("Введите Ваш возраст:")
age = input()
with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
    driver.get("https://52.armbos.ru")
    driver.find_element(By.ID, "test_user_login").send_keys(login)
    driver.find_element(By.ID, "test_user_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(1)
    try:
        if gender == 'male':
            Select(driver.find_element(By.ID, "test_user_sex")).select_by_value('male')
        driver.find_element(By.CLASS_NAME, "numeric").send_keys(age)
        driver.find_element(By.CLASS_NAME, "form-actions").click()
    except:
        ...
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, "w-100").click()
    except:
        ...
    time.sleep(1)

    answers = {3: 'Скорее не согласен', 5: 'Без мнения', 7: 'Скорее согласен'}
    try:
        for i in range(170):
            driver.find_element(By.XPATH,'//*[@title="%s"]' % answers[random.randrange(3, 8, 2)]).click()
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "btn-success").click()
            time.sleep(5)
    except:
        ...
    print("Готово")

