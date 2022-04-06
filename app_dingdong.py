# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

pay_pwd = '123456'

desired_caps = dict(
    platformName='Android',
    platformVersion='12',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    appPackage='com.yaya.zone',
    appActivity='cn.me.android.splash.activity.SplashActivity',
    noReset=True,
    resetKeyboard=True,
    unicodeKeyboard=True,
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def find_element_by_id(element_id):
    print("find_element_by_id")
    if element_id is None:
        return None
    while True:
        try:
            element = driver.find_element_by_id(element_id)
            if element:
                break
            time.sleep(0.1)
        except NoSuchElementException:
            print("find_element_by_id:" + element_id + " NoSuchElementException")
            time.sleep(0.1)
    return element


def find_elements_by_id(elements_id):
    if elements_id is None:
        return None
    while True:
        try:
            element = driver.find_elements_by_id(elements_id)
            if element:
                break
        except NoSuchElementException:
            print("find_elements_by_id:" + elements_id + " NoSuchElementException")
            time.sleep(0.1)
    return element


def skip_advertisement():
    time.sleep(0.2)
    find_element_by_id("com.yaya.zone:id/tv_skip").click()


def enter_shopping_cart():
    time.sleep(1)
    find_element_by_id("com.yaya.zone:id/ani_car").click()


def confirm_order():
    find_element_by_id("com.yaya.zone:id/btn_submit").click()


def auto_pay():
    submit_element = find_element_by_id("com.yaya.zone:id/tv_submit")
    if submit_element:
        while True:
            submit_element.click()
            if select_appointment():
                break
            time.sleep(0.2)
        # select_payment_method()
        find_element_by_id("com.yaya.zone:id/tv_submit").click()
        # need to use appium-inspector to view ali pay & weChat pay button("确认支付") then press pwd
        press_pay_pwd()


def select_appointment():
    # 选择时间
    select_hour_root_elements = find_elements_by_id("com.yaya.zone:id/cl_item_select_hour_root")
    for root_element in select_hour_root_elements:
        title_element = root_element.find_element_by_id("com.yaya.zone:id/tv_item_select_hour_title")
        desc_element = root_element.find_element_by_id("com.yaya.zone:id/tv_item_select_hour_desc")
        if desc_element.text != "已约满":
            root_element.click()
            print("预约时间：" + title_element.text)
            return True
    # 关闭
    find_element_by_id("com.yaya.zone:id/iv_dialog_select_time_close").click()
    return False


def select_payment_method():
    """
    TODO 支持选择支付方式
    :return:
    """
    find_element_by_id("com.yaya.zone:id/rl_pay_type")


def press_pay_pwd():
    """
    模拟输入支付密码
    :return:
    """
    if pay_pwd is None:
        return
    for number in pay_pwd:
        driver.press_keycode(int(number) + 7)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    skip_advertisement()
    enter_shopping_cart()
    confirm_order()
    auto_pay()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
