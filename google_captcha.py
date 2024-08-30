

from DrissionPage import ChromiumPage from RecaptchaSolver import Recaptcha5olver
import time
driver ChromiumPage()
recaptchaSolver RecaptchaSolver(driver)
driver.get("https://www.google.com/recaptcha/ap12/demo")
to time.time()
recaptchasolver.solveCaptcha()
print("Time to solve the captcha: (time.time()-10:.21) seconds")
driver.ele("#recaptcha-demo-submit").click()
driver.close()
