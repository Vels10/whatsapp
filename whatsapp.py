from selenium import webdriver

driver = webdriver.Chrome("C:/Users/vels10/Downloads/chromedriver.exe")     # Download Chromedriver and initialize with the path                      
driver.get('https://web.whatsapp.com/')                                     # Browser for Whatsapp

name = input('Enter the name of user or group : ')                          # Group Name
msg = input('Enter your message : ')                                        # Enter the Message you want to send
count = int(input('Enter the count : '))                                    # N number of messages it send

input('Enter anything after scanning QR code')                                  

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))   # xpath of the group name
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')                       #(div -> class name ('_13mgz')) Eg: it will be (<div tabindex "-1" class = "_13mgZ"> == $0)
 

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')                    #Send Button Class name Eg: <button class = "_3M-N-">...</button> == $0
    button.click()

