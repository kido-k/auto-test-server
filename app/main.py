from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

WAIT_TIME = 20

if __name__ == '__main__':
    print("start")
    # Selenium サーバーへ接続する。
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        desired_capabilities=DesiredCapabilities.CHROME.copy()
    )
    # 任意のHTMLの要素が特定の状態になるまで待つ
    # ドライバとタイムアウト値を指定
    print("wait")
    wait = WebDriverWait(driver, WAIT_TIME)
    driver.set_window_size(1280, 1024)

    # ------ ここから自動開始 ---------
    # サイトにアクセスにアクセス
    print("get")
    driver.get("https://googole.com")
    
    # メールアドレスの入力
    input_mail_address = driver.find_element(By.ID, "mail_address")
    input_mail_address.send_keys("hoge@example.co.jp")
    print("input mail")

    # パスワードの入力
    input_mail_password = driver.find_element(By.ID, "password")
    input_mail_password.send_keys("password")
    print("input password")

    driver.save_screenshot("./image/login.png")

    # ログインボタンを押下
    button_login = driver.find_element(By.ID, "login_button")
    button_login.click()
    print("login button")

    # ログイン後のページ遷移
    wait.until(
        presence_of_element_located((By.CLASS_NAME, "widget__wrap")))
    driver.save_screenshot("./image/top.png")
    
    print("finish")
    # ------ ここまで ---------

    driver.quit()
