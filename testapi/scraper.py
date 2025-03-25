from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def generate_image(text):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Headless mode (UI නොදැක්කම run කරන්න)
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://ephoto360.com/")

    try:
        input_box = driver.find_element(By.NAME, "your_text")
        input_box.send_keys(text)
        input_box.send_keys(Keys.RETURN)

        time.sleep(5)  # Image generate වෙන්න වෙලා දෙන්න

        img_element = driver.find_element(By.TAG_NAME, "img")
        img_url = img_element.get_attribute("src")
        
        return img_url
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        driver.quit()
