from appium import webdriver


class Driver:
    def getDriverMethod(self):
        # Part 1: Desired capabilities
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '12'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = 'Pixel 6 Pro'
        desired_caps['app'] = ('D:/Android APK for demo/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        # Part 2: "Webdriver Object"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
