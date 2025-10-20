from selenium import webdriver #Метод get_attribute 
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

     # 1. Найти элемент-картинку (сундук)
    treasure_img = browser.find_element(By.CSS_SELECTOR, "#treasure")
    
    # 2. Взять значение атрибута valuex
    x_value = treasure_img.get_attribute("valuex")
    
    # 2. Вычислить математическую функцию
    y = calc(x_value)
    
    # 3. Ввести ответ в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[class]")
    button.click()

    print("Тест прошел!")

except Exception as e:
    print(f"Тест упал: {e}")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()