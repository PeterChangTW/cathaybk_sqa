import pytest
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

# 瀏覽器
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1600, 900)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

# 截圖
def screenshot(browser, test_name):
    directory = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(directory):
        os.makedirs(directory)
    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(directory, f"screenshot_{date_time}_{test_name}.png")
    browser.save_screenshot(screenshot_path)

def test_open_website(browser):
    # 1 開啟國泰世華官方網站 (https://www.cathaybk.com.tw/cathaybk) 成功前往國泰世華官網頁面
    browser.get("https://www.cathaybk.com.tw/cathaybk")
    assert browser.current_url == "https://www.cathaybk.com.tw/cathaybk"
    screenshot(browser, test_open_website.__name__)

def test_click_newaccount(browser):
    # 2 點擊 [開戶] 引導至開戶提示頁
    button = browser.find_element(By.CSS_SELECTOR, "div.cubre-o-quickLink > div:nth-child(1)")
    button.click()
    assert browser.current_url == "https://www.cathaybk.com.tw/cathaybk/personal/product/deposit/open-account/"
    screenshot(browser, test_click_newaccount.__name__)

def test_click_cubeapp(browser):
    # 3.1 成功另開分頁，前往下載CUBE App頁面
    button = browser.find_element(By.CSS_SELECTOR, "a.cubre-m-anchor__btn.swiper-slide.swiper-slide-next")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "section[data-anchor-block='blockName02'] #lnk_MajorButtonLink")
    browser.execute_script("arguments[0].scrollIntoView();", button)
    time.sleep(1)
    screenshot(browser, f"{test_click_newaccount.__name__}_1")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == "https://www.cathaybk.com.tw/cathaybk/promo/event/ebanking/product/appdownload/index.html"

    # 3.2 Android與iOS版本號須一致
    android_version = browser.find_element(By.CSS_SELECTOR, "#android").text.split('：')
    ios_version = browser.find_element(By.CSS_SELECTOR, "#ios").text.split('：')
    assert android_version[1] == ios_version[1]
    screenshot(browser, f"{test_click_newaccount.__name__}_2")

    # 3.3 下載 Cube App的QR Code icon高寬均為160px
    qrcode_image_element = browser.find_element(By.CSS_SELECTOR, ".download-qrcode img")
    assert qrcode_image_element.size['width'] == 160
    assert qrcode_image_element.size['height'] == 160
    screenshot(browser, f"{test_click_newaccount.__name__}_3")

    # 3.4 切換為行動版(Webview)時，QR Code不顯示於畫面
    browser.set_window_size(430, 932)
    assert qrcode_image_element.get_attribute("src") != ""
    screenshot(browser, f"{test_click_newaccount.__name__}_4")
