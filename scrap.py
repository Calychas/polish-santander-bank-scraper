import selenium.webdriver as webdriver
import time
from selenium.webdriver.common.by import By
import random

def random_sleep(min: int = 1):
    time.sleep(random.random() * 3 + min)

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.centrum24.pl/centrum24-web/login")
input("\n\n=========== Click here in the terminal when you're logged in ============\n\n\n")

# Historia
driver.find_element(By.ID, "menu_multichannel_your_finances").click()
random_sleep()

# Przeglad wydatkow
driver.find_element(By.ID, "menu_multichannel_pfm_expenses_sub").click()
random_sleep()

# Okres
driver.find_element(By.XPATH, '//*[@id="history-filter-box"]/div[2]/div/span[2]/div/button').click()
random_sleep()

# Cala dostepna historia
driver.find_element(By.XPATH, '//*[@id="history-filter-box"]/div[2]/div/span[2]/div/div/ul/li[7]').click()
random_sleep()

# Kategorie wydatkow
driver.find_element(By.XPATH, '//*[@id="history-filter-box"]/div[2]/div/span[3]/div/button').click()
random_sleep()

# Wszystkie wydatki i pominiete transakcje
driver.find_element(By.XPATH, '//*[@id="history-filter-box"]/div[2]/div/span[3]/div/div/ul/li[2]').click()
random_sleep()

# Zapisz strone i kliknij Nastepne
i = 0
time.sleep(5)
while True:
    with open(f'pages/page_{i:04}.html', 'w+') as f:
        f.write(driver.page_source)
    driver.find_element(By.XPATH, '//*[@id="transactionList"]/div[2]/div/div/table/tfoot/tr/td[2]/ul/li[2]/a').click()
    random_sleep(3)
    i = i + 1

# Should crash with selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="transactionList"]/div[2]/div/div/table/tfoot/tr/td[2]/ul/li[2]/a"}
# as the Nastepne button disappears