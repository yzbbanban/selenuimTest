from selenium import webdriver

broswer = webdriver.Chrome()

broswer.implicitly_wait(10)

broswer.get('https://www.taobao.com')
input_first = broswer.find_element_by_id('q')
input_second = broswer.find_element_by_css_selector('#q')
input_third = broswer.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)

input_first.send_keys('macbook pro')
button=broswer.find_element_by_class_name('btn-search')
button.click()
print(broswer.page_source)


broswer.close()

