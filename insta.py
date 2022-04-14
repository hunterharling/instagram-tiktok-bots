from selenium import webdriver
from utils import wait
import time
from credentials import INSTA_USER, INSTA_PASS

# mass follow+unfollow
URL = 'https://www.instagram.com'

class InstaBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    
    def login(self):
        bot = self.bot
        bot.get(URL)
        time.sleep(3)

        email_input = bot.find_elements_by_tag_name('input')[0]
        pw_input = bot.find_elements_by_tag_name('input')[1]

        email_input.clear()
        pw_input.clear()

        email_input.send_keys(self.username)
        wait()
        pw_input.send_keys(self.password)

        pw_input.submit()
        print("logging in...")
        time.sleep(4)

        page = bot.find_elements_by_tag_name('body')[0]
        if 'Save Your Login Info?' in page.get_attribute('textContent'):
            ignore_btn = bot.find_elements_by_tag_name('button')[1]
            ignore_btn.click()
            wait()
        
        page1 = bot.find_elements_by_tag_name('body')[0]
        if 'Turn on Notif' in page1.get_attribute('textContent'):
            bot.find_elements_by_class_name('aOOlW')[1].click()
            wait()
            
    def navigate_to_profile(self):
        bot = self.bot
        profile_btn = bot.find_elements_by_class_name('qNELH')[-1]
        profile_btn.click()
        wait()

        link = bot.find_elements_by_class_name('-qQT3')[0]
        link.click()
        time.sleep(3)

    def remove_bad_followers(self):
        print("navigating to profile...")
        wait()
        self.navigate_to_profile()
        bot = self.bot

        # followers
        followers_btn = bot.find_elements_by_tag_name('a')[1]
        followers_btn.click()
        print("getting followers...")
        wait()

        followers = []
        followers_list = bot.find_elements_by_tag_name('ul')[-1] \
            .find_elements_by_tag_name('div')[0] \
                .find_elements_by_tag_name('li')
        for f in followers_list:
            followers.append(f.get_attribute('textContent').split(' ')[0])

        close = bot.find_elements_by_class_name('QBdPU')[-1]
        print("closing popup...")
        close.click()
        wait()
        
        # following
        following_btn = bot.find_elements_by_tag_name('a')[2]
        print("opening popup...")
        following_btn.click()
        wait()

        following_list = bot.find_elements_by_tag_name('ul')[-1] \
            .find_elements_by_tag_name('div')[0] \
                .find_elements_by_tag_name('li')

        # remove
        count = 0
        for u in following_list:
            follower_is_good = False
            u_username = u.get_attribute('textContent').split(' ')[0]

            for e in followers:
                if e == u_username:
                    follower_is_good = True

            if not follower_is_good and count < 125:
                remove_btn = u.find_elements_by_tag_name('button')[0]
                remove_btn.click()
                print("removing follow...")
                wait()

                remove_btn1 = bot.find_elements_by_class_name('-Cab_')[0]
                remove_btn1.click()
                wait()
                count += 1
        
        close2 = bot.find_elements_by_class_name('QBdPU')[-1]
        print("closing popup...")
        close2.click()
        wait() 


user = InstaBot(INSTA_USER, INSTA_PASS)
user.login()
wait()
user.remove_bad_followers()
print('---------- DONE ----------')
