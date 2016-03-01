from selenium import webdriver

browser = webdriver.Firefox()
#browser.get('http://purpleinkllc.com/blog/name-claim-and-aim-your-strengths/#sthash.LOcO2LLy.ZtwyFN9w.dpbs')

browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(20) > li:nth-child(1) > a:nth-child(1)')

elem.click()

elems = browser.find_elements_by_css_selector('p')
len(elems)
