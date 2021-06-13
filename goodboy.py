from selenium import webdriver
browser = webdriver.Chrome('/Users/Frankie/Html-Css-Javascript/walkinwardrobe/chromedriver')
browser.implicitly_wait(10)
browser.get('https://frankli-n.github.io/walkinwardrobe/')
browser.switch_to.frame(browser.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]')) # switch to iframe
button = browser.find_element_by_xpath('//button[@aria-label="Play"]') # look for button
button.click()