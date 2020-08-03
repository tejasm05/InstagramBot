from selenium import webdriver
from time import sleep
from pynput import mouse
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition
import random
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
actions = ActionChains(driver)
# Comment_List = ['Wow!!', 'Cool! ^o^', 'Wow!!', 'Nishcheee!', 'Crazy!', 'T_T', 'Great!!', 'Beautiful!', 'Wow!',
# # #                 'That looks amazing!! <3', "I'm fantasized", "Wow you're so good!!"]
Comment_List = ["Follow 4 Follow back :)","Nice!!","Follow4fFollowback :)","Beautiful","COOL!"]
keyboard = Controller()
tabs_open = 0
posts_reached = ['1']
notnowover = False
z = int(input('How many old posts do you wanna reach?(Input type (Number)) Enter a number here if you had run the bot before and it crashed.. this skips to the number of posts you liked before so that you do not unlike. If you do not know what this is type 0 and press enter!'))

reaching_old_post = range(z)
reachedOldPost = False
coming_out_ofloop = False
file_opened = False
int1 = 0
mouse = mouse.Controller()
users_gettingfollowed = []
random_num = range(1,4)
reachedoldpost = False
random_ans = ''
comment_count = 0


def Initiate_InstagramBot():

    LoginButton = False
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    driver.maximize_window()
    WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.NAME, "username")))
    assert 'Instagram' in driver.title
    uname = driver.find_element_by_name('username')
    WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.NAME, "password")))
    passwrd = driver.find_element_by_name('password')
    WebDriverWait(driver,12).until(condition.element_to_be_clickable((By.NAME,"username")))
    uname.click()
    uname.send_keys('just_cuddle_baby')
    WebDriverWait(driver,12).until(condition.element_to_be_clickable((By.NAME,"password")))
    passwrd.click()
    passwrd.send_keys('onlyfoolslose')

    while LoginButton == False:
        try:
            def login_get():
                try:
                    WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")))
                    log_in = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
                    log_in.click()
                except NoSuchElementException:

                    WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.CLASS_NAME,"                    Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ")))
                    log_in = driver.find_element_by_class_name("                    Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ")
                    log_in.click()
                except ElementClickInterceptedException:
                    login_get()
                except TimeoutError:
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()

            login_get()

        except NoSuchElementException:
            WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")))
            login_get()

        else:
            LoginButton = True

    def ProceedToSearch():
        sleep(2)
        global notnowover
        if notnowover != True:
            try:
                def NOTNOW(): #dont save login info
                    global notnowover
                    WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
                    notnow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
                    notnow.click()
                    notnowover = True
                NOTNOW()
            except NoSuchElementException:
                WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.CLASS_NAME, "sqdOP yWX7d    y3zKF     ")))
                notnow = driver.find_element_by_class_name("sqdOP yWX7d    y3zKF     ")
                notnow.click()
            except ElementClickInterceptedException:
                sleep(3)
                NOTNOW()
        # se
    # archbutton variable actually points to the Pop up by instagram on login from browser. It matches to the not now button
        sleep(3)
        try:
            def dontturnonnotifs():
                WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
                notificationno = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
                notificationno.click()
            dontturnonnotifs()

        except NoSuchElementException:
            WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.CLASS_NAME, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
            notificationno = driver.find_element_by_class_name('/html/body/div[4]/div/div/div/div[3]/button[2]')
            notificationno.click()
        except ElementClickInterceptedException:
            sleep(2)
            try:
                dontturnonnotifs()
            except:
                WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.CLASS_NAME, "aOOlW   HoLwm ")))
                notificationno = driver.find_element_by_class_name('aOOlW   HoLwm ')
                notificationno.click()

    ProceedToSearch()

    WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")))
    searchbutton1 = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    searchbutton1.send_keys('#aesthetic')

    WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div")))
    hashcodepage = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div')
    hashcodepage.click()
    try:
        def getfirstpost():
            WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]")))
            post = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
            post.click()
        getfirstpost()
    except TimeoutError:
        WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.CLASS_NAME, "_9AhH0")))
        driver.find_element_by_class_name("_9AhH0").click()
    except NoSuchElementException:
        WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.CLASS_NAME, "_9AhH0")))
        driver.find_element_by_class_name("_9AhH0").click()

def follow():
    try:
        WebDriverWait(driver, 12).until(condition.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button")))
        # following = False
        followcheck = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button").text
        str(followcheck)
        print(followcheck)

    except NoSuchElementException:
        followcheck = driver.find_element_by_class_name("sqdOP yWX7d     _8A5w5    ").text
        str(followcheck)

    if followcheck == "Following":
        next_post()
        # following = True
    else:
        try:
            WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button")))
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button").click()

        except NoSuchElementException:
            next_post()
        except:
            next_post()
    followcheck = ""


def comment():
    global comment_count
    if comment_count <= 7:
        try:
            # if (len(driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[3]/div')) != 0 or len(driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')) == 0) :
            #     sleep(3)

            choice = random.choice(Comment_List)
            choicenew = str(choice)
            WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/textarea")))

            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/textarea').click()
            keyboard.type(choicenew)
            sleep(1)
            comment_count += 1
            try:
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/button').click()
            except NoSuchElementException:
                sleep(1)
                next_post()
            except ElementClickInterceptedException:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            comment_count += 1
        except:
            sleep(15)
    else:
        comment_count = 0







def next_post():
    try:
        WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]")))
        nextpost = driver.find_element_by_xpath("//*[contains(text(),'Next')]")
        nextpost.click()
    except NoSuchElementException or ElementClickInterceptedException:
        driver.find_element_by_class_name(" _65Bje  coreSpriteRightPaginationArrow").click()

def LikePost():
    try:
        sleep(2)
        WebDriverWait(driver, 12).until(condition.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button")))

        like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button")
        like.click()
    except NoSuchElementException:
        sleep(2)
        next_post()
    except ElementNotInteractableException:
        next_post()
    except ElementClickInterceptedException:
        next_post()

def reacholdpost():
    global reachedOldPost, coming_out_ofloop
    if reachedOldPost == False:
        for i in reaching_old_post:
            next_post()
            sleep(1.5)
            i += 1
            reachedOldPost = True
    if coming_out_ofloop == True:
        sleep(10)
        coming_out_ofloop = False

def Randomized_loop():
    global reachedoldpost
    try:

        while True:
            if reachedoldpost != True:
                reacholdpost()
                reachedoldpost = True
                sleep(1)
            sleep(3)
            LikePost()
            sleep(0.5)
            if (random_ans == 'y' or follow_choice == "y"):
                follow()
                sleep(1)
            else:
                pass
            sleep(0.3)
            sleep(2)
            try:
                if random_ans == 'y':
                    comment()
                elif comment_choice == 'y':
                    comment()
                else:
                    pass
            except:
                next_post()
            sleep(1)
            next_post()
    except:
        next_post()
        next_post()
        next_post()
        next_post()
        next_post()
        Randomized_loop()



print('''

Welcome to Instagram Bot ^-^. This bot likes and comments on people's posts and follows the users too. Use it to increase your popularity and gain some free followers :3

* This bot is NOT PERFECT, IT CAN CRASH don't panic! Just rerun the bot and you'll be fine.

Though the chances are extremely less. Cus this is made by Light. Follow Instagram = @just_cuddle_baby

LOVE ℒḯ❡н⊥
(give input below to start bot)

''')
random_ans = input('Do you want to randomize the functions [Like,Follow,Comment] [y/n]')

if random_ans == 'y':
    Initiate_InstagramBot()
    Randomized_loop()
else:
    follow_choice = input('Do you want to follow? [y/n]')
    comment_choice = input('Do you want to comment?[y/n]')
    Initiate_InstagramBot()
    Randomized_loop()
