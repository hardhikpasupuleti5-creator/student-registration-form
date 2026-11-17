
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8082")

    driver.maximize_window()

    driver.find_element(By.ID, "name").send_keys("Sai Hardhik")
    driver.find_element(By.ID, "email").send_keys("hardhik@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("9876543210")

    Select(driver.find_element(By.ID, "gender")).select_by_visible_text("Male")
    Select(driver.find_element(By.ID, "course")).select_by_visible_text("AIML")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    message = driver.find_element(By.ID, "message").text

    assert "Registration Successful" in message

    print("TEST PASSED: Student Registration Successful")

finally:
    driver.quit()
