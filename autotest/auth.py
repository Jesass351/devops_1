from selenium.webdriver.common.by import By

def auth(driver):
    result_login = login(driver)
    if not result_login:
        return False
    
    return True


def login(driver):
    try:
        data = {
            'login':'admin',
            'password':'admin'
        }
        driver.get("http://127.0.0.1:5000/auth/login")
        input_username = driver.find_element(By.ID, "login")
        input_password = driver.find_element(By.ID, "password")
        input_username.send_keys(data['login'])
        input_password.send_keys(data['password'])
        driver.find_element(By.XPATH, "/html/body/main/div/form/button").click()
        if "Вход выполнен успешно" in driver.find_element(By.XPATH, "/html/body/div/div").text:
            return True
        else:
            return False
    except:
        return False