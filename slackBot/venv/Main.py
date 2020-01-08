from slackbot.bot import Bot
from slacker import Slacker
import math
import slackbot_settings
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from selenium.common.exceptions import NoSuchElementException
import time


def main():
    slack = Slacker(slackbot_settings.API_TOKEN)

    print("取得します")
    options = ChromeOptions()
    options.add_argument('--headless')
    driver = Chrome(options=options)
    driver.get('https://hcms.hosei.ac.jp/')
    print("取得中...")
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    driver.find_element_by_xpath("//*[@id='username']").send_keys("19x3157")
    driver.find_element_by_xpath("//*[@id='password']").send_keys("X2y57JPf")
    driver.find_element_by_css_selector("button.form-element.form-button").click()
    driver.implicitly_wait(10)
    print("ログイン完了")
    iframe = driver.find_element_by_xpath("//*[@id='Main46dc03dbxaccex4553x867cxd1f69a7656b1']")
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    time.sleep(1)
    try:
        size = len(
            driver.find_element_by_xpath("/html/body/div/form/table/tbody").find_elements_by_tag_name('tr'))
    except NoSuchElementException:
        print('エラー')
        return
    list1 = [[0 for i in range(2)] for j in range(size - 1)]
    print("課題取得中")
    for i in range(size - 1):
        name = driver.find_element_by_xpath(
            "/html/body/div/form/table/tbody/tr[" + str(i + 2) + "]/td[4]").text
        list1[i][0] = name
        due = driver.find_element_by_xpath(
            "/html/body/div/form/table/tbody/tr[" + str(i + 2) + "]/td[3]").text
        list1[i][1] = due
    print("取得完了")
    temp = max(list1[:], key=len)
    Max = max(temp, key=len)
    headers = ["教科", "期限"]
    for i in range(len(list1)):
        leftTime = math.ceil(
            (datetime.datetime.strptime(list1[i][1], "%Y/%m/%d %H:%M") - datetime.datetime.now()).seconds / 3600)
        if leftTime == 2:
            text = list1[i][0] + "あと" + str(leftTime) + "時間ですよ"
            slack.chat.post_message('URZM8NGHY', str(text), as_user=True)
    slack.chat.post_message('URZM8NGHY', "テストです", as_user=True)
    driver.quit()


if __name__ == "__main__":
    print('starting slackbot')
    main()
