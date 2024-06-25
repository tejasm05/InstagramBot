from selenium import webdriver
from time import sleep
from pynput import mouse
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
from datetime import datetime


driver = webdriver.Chrome(executable_path="chromedriver.exe")
actions = ActionChains(driver)
Comment_List = ['Wow!!', 'Cool! ^o^','Wow!!', 'Nishcheee!','T_T', 'Great!!', 'Beautiful!', 'Wow!','That looks amazing!! <3', "I'm fantasized",  "Wow you're so good!!"]
keyboard = Controller()
tabs_open = 0
posts_reached = ['1']


z = int(input('How many old posts do you wanna reach?(Input type (Number)) Enter a number here if you had run the bot before and it crashed.. this skips to the number of posts you liked before so that you do not unlike. If you do not know what this is type 0 and press enter!'))


reaching_old_post = range(z)
reachedOldPost = False
coming_out_ofloop = False
file_opened = False
int1  = 0
mouse = mouse.Controller()
users_gettingfollowed = []
random_num = (1,2,3)
reachedoldpost = False
random_ans = ''




def Initiate_InstagramBot():
    LoginButton = False
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    driver.maximize_window()
    sleep(2)
    assert 'Instagram' in driver.title
    uname = driver.find_element_by_name('username')
    passwrd = driver.find_element_by_name('password')
    uname.click()
    uname.send_keys('#Enter Your Username')
    passwrd.click()
    passwrd.send_keys('#Enter Your Password')
    while LoginButton == False:
        try:
            def login_get():
                try:
                    log_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
                    log_in.click()
                except NoSuchElementException:
                    sleep(1)
                except ElementClickInterceptedException:
                    sleep(1)

            login_get()

        except NoSuchElementException:
            sleep(2)
            login_get()
        else:
            LoginButton = True
    sleep(4)
    

    def ProceedToSearch():
        # searchbutton variable actually points to the Pop up by instagram on login from browser. It matches to the not now button
        searchbutton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        searchbutton.click()
    try:
        ProceedToSearch()
    except NoSuchElementException:
        sleep(2)
        ProceedToSearch()
    sleep(1)
    searchbutton1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    searchbutton1.send_keys('the name of whichever hashtag you want to like or comment posts from')
    sleep(3)
    hashcodepage = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')
    hashcodepage.click()
    sleep(1.5)
    sleep(3)
    post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    post.click()

    
def follow():
    try:
        try:
            followbutton = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            followbutton.click()

            if len(driver.find_elements_by_xpath('/html/body/div[5]/div/div')) > 0:
                cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
                cancel.click()
        except NoSuchElementException:
            sleep(2)
            followbutton = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            followbutton.click()

            if len(driver.find_elements_by_xpath('/html/body/div[5]/div/div')) > 0:
                cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
                cancel.click()
        except ElementClickInterceptedException:
            mouse.position(1000,1000)
            mouse.click()
            followbutton = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            followbutton.click()

            if len(driver.find_elements_by_xpath('/html/body/div[5]/div/div')) > 0:
                cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
                cancel.click()
    except NoSuchElementException:
        next_post()
        next_post()


def comment():
    global comment_count
    comment_count = 0
    if comment_count <= 6:
        if len(driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[3]/div')) != 0:

            follow()
            nextpost = driver.find_element_by_xpath("//*[contains(text(),'Next')]")
            nextpost.click()

            sleep(3)
        elif len(driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')) == 0:
            follow()
            nextpost = driver.find_element_by_xpath("//*[contains(text(),'Next')]")
            nextpost.click()
            sleep(3)
        else:
            sleep(3)
            choice = random.choice(Comment_List)
            choicenew = str(choice)
            sleep(0.5)
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
            keyboard.type(choicenew)
            comment_count+= 1
            try:
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()

            except NoSuchElementException:
                sleep(1)
                next_post()
            except ElementClickInterceptedException:
                try:
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                except ElementClickInterceptedException or NoSuchElementException:
                    next_post()
            except ElementNotInteractableException:
                sleep(15)
                next_post()
                next_post()

    else:

        sleep(20)
        comment_count = 0


def openprofile():
    global tab
    try:
        sleep(3)
        userprofile = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a')
        openlinkinnewtab = Keys.LEFT_CONTROL, Keys.ENTER
        userprofile.send_keys(openlinkinnewtab)
    except NoSuchElementException:
        sleep(2)
        userprofile = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a')
        openlinkinnewtab = Keys.LEFT_CONTROL, Keys.ENTER
        userprofile.send_keys(openlinkinnewtab)


def next_post():
    nextpost = driver.find_element_by_xpath("//*[contains(text(),'Next')]")
    nextpost.click()

def LikePost():
    try:
        like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
        like.click()
    except NoSuchElementException:
        next_post()
    except ElementNotInteractableException:
        next_post()
    except ElementClickInterceptedException:
        next_post()
def maketextfile():
    global file_opened, int1
    if file_opened == True:
        with open("Log.txt", 'a') as the_appended_file:
            for post in posts_reached:
                the_appended_file.write("\n")
                the_appended_file.write(post)
            file_opened = False
            int1 += 1
            posts_reached.append(str(int1))
    else:
        with open("Log.txt", 'w') as the_appended_file:
            for post in posts_reached:
                the_appended_file.write("\n")
                the_appended_file.write(post)
            int1 += 1
            posts_reached.append(str(int1))

def reacholdpost():
    global reachedOldPost,coming_out_ofloop
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
    global  reachedoldpost
    while True:
        choice = random.choice(random_num)
        if choice == 1:
            if reachedoldpost != True:
                reacholdpost()
                reachedoldpost= True
            sleep(3)
            LikePost()
            sleep(0.5)
            if random_ans == 'y':
                follow()
            elif follow_choice== 'y':
                follow()
            else:
                pass
            sleep(0.3)
            if random_ans == 'y':
                comment()
            elif comment_choice== 'y':
                comment()
            else:
                pass
            sleep(1)
            maketextfile()
            sleep(2)
            next_post()
            print(str(int1)+' followed')
        elif choice == 2:
            if reachedoldpost != True:
                reacholdpost()
                reachedoldpost = True
            sleep(3)
            LikePost()
            sleep(2)
            maketextfile()
            next_post()
            print(str(int1)+' not followed')
        elif choice == 3:
            sleep(7)
            currenttime = datetime.now()
            print(currenttime)
            next_post()


print('''
Welcome to Instagram Bot ^-^. This bot likes and comments on people's posts and follows the users too. Use it to increase your popularity and gain some free followers
(give input below to start bot)
''')
random_ans= input('Do you want to randomize the functions [Like,Follow,Comment] [y/n]')

if random_ans == 'y':
    Initiate_InstagramBot()
    Randomized_loop()
else:
    follow_choice = input('Do you want to follow? [y/n]')
    comment_choice = input('Do you want to comment?[y/n]')
    Initiate_InstagramBot()
    Randomized_loop()