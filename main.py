import urllib3
from bs4 import BeautifulSoup
import subprocess
import os

class StoryTitle:
    def __init__(self, title, link):
        self.title = title
        self.link = f'https://old.reddit.com{link}'

class SubredditBot:
    def read_post(self, link):
        response = self.http.request('GET', link)
        html_string = response.data.decode("utf-8") 
        soup = BeautifulSoup(html_string, 'html.parser')

        post = soup.find('div', attrs={"class": "expando"})
        return post.text

    def fetch_posts(self):
        response = self.http.request('GET', self.url)
        html_string = response.data.decode("utf-8") 
        soup = BeautifulSoup(html_string, 'html.parser')

        stories = []
        for storyTitle in soup.find_all('a', attrs={"data-event-action": "title"}):
            story = StoryTitle(storyTitle.text, storyTitle.get('href'))
            stories.append(story)
        
        return stories


    def __init__(self, url):
        self.url = url
        self.http = urllib3.PoolManager()

# The following are placeholder values
url = 'https://old.reddit.com/r/relationship_advice/rising/' #can be any subreddit, MAKE SURE to use old.reddit.com
subredditBot = SubredditBot(url)

# This post is very short, that's why I picked it
postText = subredditBot.read_post('https://old.reddit.com/r/offmychest/comments/195pgr5/i_told_my_dog_that_she_is_adopted_and_i_feel_bad/')

output_path = os.path.abspath('output')
with open(f'{output_path}/text.txt', 'w') as f:
    f.write(postText)

# Set the session id securely (see comments in get_voiceover.sh)
session_id = os.environ.get('TIKTOK_SESSION_ID')

subprocess.call(['chmod', '+x', 'get_voiceover.sh'])
subprocess.check_call(['./get_voiceover.sh', 'output/text.txt', session_id])