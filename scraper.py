from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import pandas as pd
from config import BASE_URL

def _extracted_from_startScraping_8(chrome_options):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options,
    )
    driver.get(BASE_URL)
    sleep(10)
    actions=ActionChains(driver)
    year=""
    make=""
    model=""
    diameter=""
    pcd=""
    offset=""
    for i in range(56):
        try:
            driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleYear-container\']").click()
            actions.send_keys(Keys.DOWN).perform()
            actions.send_keys(Keys.ENTER).perform()
        except Exception as e:
            driver.close()
        sleep(1)
        try:
            year=driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleYear-container\']").text
            print(year)
            driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleMake-container\']").click()
        except Exception as e:
            driver.close()
        # sleep(2)
        make_elements=driver.find_element(By.CSS_SELECTOR,"ul[id=\'select2-searchVehicleMake-results\']").find_elements(By.TAG_NAME,"li")
        try:
            
            driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleMake-container\']").click()
        except Exception as e:
            driver.close()
        del make_elements[0]
        for make_element in make_elements:
            try:
                driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleMake-container\']").click()
                actions.send_keys(Keys.DOWN).perform()
                actions.send_keys(Keys.ENTER).perform()
            except Exception as e:
                driver.close()
            sleep(1)
            try:
                make=driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleMake-container\']").text
                driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleModel-container\']").click()
            except Exception as e:
                driver.close()
            model_elements=driver.find_element(By.CSS_SELECTOR,"ul[id=\'select2-searchVehicleModel-results\']").find_elements(By.TAG_NAME,"li")
            driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleModel-container\']").click()
            del model_elements[0]
            for model_element in model_elements:
                try:
                    driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleModel-container\']").click()
                    actions.send_keys(Keys.DOWN).perform()
                    actions.send_keys(Keys.ENTER).perform()
                except Exception as e:
                    driver.close()
                sleep(1)
                try:
                    model=driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleModel-container\']").text
                    driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleDiameter-container\']").click()
                    
                except Exception as e:
                    driver.close()
                diameter_elements=driver.find_element(By.CSS_SELECTOR,"ul[id=\'select2-searchVehicleDiameter-results\']").find_elements(By.TAG_NAME,"li")
                driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleDiameter-container\']").click()
                del diameter_elements[0]
                for diameter_element in diameter_elements:
                    try:
                        driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleDiameter-container\']").click()
                        actions.send_keys(Keys.DOWN).perform()
                        actions.send_keys(Keys.ENTER).perform()
                    except Exception as e:
                        driver.close()
                    sleep(1)
                    try:
                        diameter=driver.find_element(By.CSS_SELECTOR,"span[id=\'select2-searchVehicleDiameter-container\']").text
                        submit_button=driver.find_element(By.CSS_SELECTOR,"button[name=\'search\']")
                        actions.key_down(Keys.CONTROL).click(submit_button).key_up(Keys.CONTROL).perform()
                        landing_page=driver.current_window_handle
                        wheel_page=driver.window_handles[-1]
                        driver.switch_to.window(wheel_page)
                        sleep(2)
                        garage_element=driver.find_element(By.CSS_SELECTOR,"div.flex-right.flex-row.modal__right")
                        actions.move_to_element(garage_element).click().perform()
                        sleep(15)
                        pcd_elements=driver.find_elements(By.CSS_SELECTOR,"span.additional.vehicle-pcd")
                        print(pcd_elements)
                        try:
                            pcd=pcd_elements[0].text
                            offset=pcd_elements[1].text
                            # print(pcd)
                            # print(offset)
                            existing_data = pd.read_excel('data.xlsx')
                            new_data={"year":[year],"make":[make],"model":[model],"diameter":[diameter],"pcd":[pcd],"offset":[offset]}
                            dataframe=pd.DataFrame(new_data)
                            updated_data = pd.concat([existing_data, new_data])
                            
                            updated_data.to_excel("data.xlsx",index=False)
                        except Exception as e:
                            print(e)
                        driver.close()
                        driver.switch_to.window(landing_page)
                    except Exception as e:
                        driver.close()
                        driver.switch_to.window(landing_page)
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--force-dark-mode")
chrome_options.add_argument("--start-maximized")
try:
    _extracted_from_startScraping_8(chrome_options)
except Exception as e:
        print(e)
