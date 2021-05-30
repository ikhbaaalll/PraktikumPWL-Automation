from selenium import webdriver
import json

web = webdriver.Chrome()
web.get('https://prakpwlselenium.herokuapp.com/')

with open('data.json') as f:
    data = json.load(f)

for state in data['test_case']:
    email = state['data']['email']
    emailInput = web.find_element_by_xpath(
        '/html/body/div/div/div/input[1]')
    emailInput.send_keys(email)

    password = state['data']['password']
    passwordInput = web.find_element_by_xpath(
        '/html/body/div/div/div/input[2]')
    passwordInput.send_keys(password)

    passwordConfirmation = state['data']['passwordConfirmation']
    passwordConfirmationInput = web.find_element_by_xpath(
        '/html/body/div/div/div/input[3]')
    passwordConfirmationInput.send_keys(passwordConfirmation)

    button = web.find_element_by_xpath(
        '/html/body/div/div/div/button')
    button.click()

    hasil = web.find_element_by_xpath('/html/body/div/div/div/h5')
    if(hasil.text == ''):
        print("berhasil")
    else:
        print("gagal")

    # mengkosongkan text field
    emailInput.clear()
    passwordInput.clear()
    passwordConfirmation.clear()
