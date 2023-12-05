from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


def createJobKoreaUrl(search):
    url = f"https://www.jobkorea.co.kr/Search/?stext={search}"
    return url

# 검색어 입력 및 URL 생성
search = input("검색할 키워드를 입력해주세요: ")
jobkorea_url = createJobKoreaUrl(search)

# Chrome Driver 설정
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 잡코리아 URL로 이동
driver.get(jobkorea_url)
time.sleep(1)

# 스크린샷 저장을 위한 폴더 생성
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# 채용 공고의 링크 수집
job_links = driver.find_elements(By.CSS_SELECTOR, "div.post-list-info > a.title")
links = [job.get_attribute('href') for job in job_links]

# 각 채용 공고 페이지로 이동하여 스크린샷 캡처
for idx, link in enumerate(links):
    if idx>=10:
        break
    driver.get(link)
    time.sleep(5)  # 페이지 로드를 위한 대기 시간
    driver.save_screenshot(f'screenshots/job_{idx+1}.png')

driver.quit()
