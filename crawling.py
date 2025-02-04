from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹 사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩 끝날 때 까지 10초 기다려줌

# 쇼핑 메뉴 클릭하기
browser.find_element_by_css_selector('a.nav.shop').click()

# 검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

# 검색어 입력
search.send_keys('옷')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrolly")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrolly")

    if after_h == before_h:
        break
    before_h = after_h

    # 상품 정보 div
    items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

    for item in items :
        name = item.find_element_by_css_selector(".basicList_link__1MaTN").text
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
        link = item.find_element_by_css_selector(".basicList_link__1MaTN > a").get_attribute('href')
        print(name, price, link)
