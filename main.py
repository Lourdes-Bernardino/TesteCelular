from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v8.2 (453324893)_apkpure.com.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True


if __name__ == '__main__': #aciona o script

    driver = webdriver.Remote("https://jessicav:2e5baf84-44d4-46bc-ac27-f191c5bff9fa@ondemand.us-west-1.saucelabs.com:443/wd/hub", caps)

# o script gerado automaticamente pelo appium não funcionou como demonstrado no vídeo pelo professor.
# revirei na internet e descobri que a sintaxe mudou um pouco
# antes se usava driver.find_element_by_accessibility_(etc) e agora é como coloquei abaixo

    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'8')
    el1.click()
    el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus')
    el2.click()
    el3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'5')
    el3.click()
    el4 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals')
    el4.click()
    el5 = driver.find_element(AppiumBy.ID, 'com.google.android.calculator:id/result_final')
    el5.click()

    driver.quit()