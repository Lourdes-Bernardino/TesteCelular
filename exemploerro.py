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

if __name__ == '__main__':  # aciona o script



    # conexao com o saucelabs, aponta para datacenter, meu usuario e chave (ocultos)
    driver = webdriver.Remote("segredo", caps)

    # o script gerado automaticamente pelo appium não funcionou como demonstrado no vídeo pelo professor.
    # revirei na internet e descobri que a sintaxe mudou um pouco
    # antes se usava driver.find_element_by_accessibility_(etc) e agora é como coloquei abaixo

    resultado_esperado = '13'

    # script que faz a soma
    botao_8 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '8')
    botao_8.click()
    botao_soma = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus')
    botao_soma.click()
    botao_5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '4')
    botao_5.click()
    botao_igual = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals')
    botao_igual.click()
    resultado_final = driver.find_element(AppiumBy.ID, 'com.google.android.calculator:id/result_final')

    print(f'Resultado final = {resultado_final.text} \n Resultado esperado = {resultado_esperado}')


    assert resultado_final.text == resultado_esperado

    driver.quit()

#esse teste não passa. feito só pra ver como roda com erro no saucelabs.