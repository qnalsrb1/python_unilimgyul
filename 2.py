from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class NcafeWriteAtt:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # CLI환경으로 접속하게 해줌
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\gyul\programming\python\윤희예림귤\웹브라우저 없는 스크랩핑 파싱 실습1\chromedriver_win32\chromedriver')
        self.driver.implicitly_wait(5)

        # 네이버 카페 로그인 $$ 출석 체크
        self.driver.get("들어가고 싶은 사이트 ")
        self.driver.find_element_by_name('id').send_keys("아이디")
        self.driver.find_element_by_name('pw').send_keys("비번")
        self.driver.find_element_by_xpath('xpath를 가져오면 됨').click()
        self.driver.implicitly_wait(30)
        self.driver.get("다른 사이트로 이동")
        self.driver.swich_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtiinput').send_keys('반갑습니다!')
        self.driver.find_element_by_xpath('글쓰기 네모칸 클릭').click()
        time.sleep(3)

        # 소멸자
        def __del__(self):
            # 전체 프로그램 종료
            self.driver.quit()

    if __name__ == '__main__':
        a = NcafeWriteAtt()
        start_time = time.time()
        a.writeAttendCheck()
        print("----Total %s seconds ---", %(time.time()-start_time))