from function import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# # 防止被网站识别
# chrome_options = Options()
# chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options = chrome_options)
# url = "https://www.op.gg/champions/"
# browser.get(url)

# get_all_top_brief_info(browser)
# get_all_jug_brief_info(browser)
# get_all_mid_brief_info(browser)
# get_all_ad_brief_info(browser)
# get_all_sup_brief_info(browser)


# version = get_version(browser)
# get_all_heros_pic(browser)

if __name__ == '__main__':
    # 防止被网站识别
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=chrome_options)
    url = "https://www.op.gg/champions/"
    browser.get(url)

    # 爬取
    # get_all_heros_pic(browser)
    # get_all_top_brief_info(browser)
    # get_all_jug_brief_info(browser)
    # get_all_mid_brief_info(browser)
    # get_all_ad_brief_info(browser)
    # get_all_sup_brief_info(browser)
    detail_info_from_some_position_hero(browser, some_hero = 'lucian', some_position = 'mid')