from datetime import datetime


######################## COOKIE ###############################
SESSION = []
JWT_USER_SECRET = "e8726d5e-287f-44de-a144-0133e7fa5a4f-6d6a22ae-6dfa-4f95-b27c-f1fa3f451988-7ad4bbef-3133-4a31-8f93-9525e81e9ccd"
JWT_ADMIN_SECRET = "0d9bed44-cd0b-4874-a395-e53c2f905575-8230560f-02af-4eca-8fa5-c31fbbff9226-7f684970-e84f-41e4-bade-ca866476ec5a"

######################## REGEX ###############################
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

######################## UUID ###############################
REGEX_UUID4 = '^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'

######################## USERS ###############################
now = datetime.now()
SIGNUP_DATE = now.strftime('%B %Y')

USERS = {
    "a5ea9d0c-1295-4a1e-8184-e22e50ec1914": {
        "user_id": "a5ea9d0c-1295-4a1e-8184-e22e50ec1914",
        "user_first_name": "Aicha",
        "user_last_name": "Haidara",
        "user_name": "AichaHaidara",
        "user_email": "a@a.com", 
        "user_password": "123",
        "user_profile_picture": "aicha.jpeg",
        "user_signup_date": "January 2014",
        "user_cover_image": "landscape2.jpg"
    },
    "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6": {
        "user_id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6",
        "user_first_name": "Elisha", 
        "user_last_name": "Ngoma",
        "user_name": "ElishaNgoma",
        "user_email": "elisha_ngoma@yahoo.fr", 
        "user_password": "123",
        "user_profile_picture": "elisha.jpg",
        "user_signup_date": "October 2016",
        "user_cover_image": "landscape1.jpg"
    },


     "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa2": {
        "user_id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa2",
        "user_first_name": "a", 
        "user_last_name": "aa",
        "user_name": "ElishaNgoma",
        "user_email": "elisha_ngoma@yahoo.fr", 
        "user_password": "123",
        "user_profile_picture": "elisha.jpg",
        "user_signup_date": "October 2016",
        "user_cover_image": "landscape1.jpg"
    },
     "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa8": {
        "user_id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa8",
        "user_first_name": "b", 
        "user_last_name": "bb",
        "user_name": "ElishaNgoma",
        "user_email": "elisha_ngoma@yahoo.fr", 
        "user_password": "123",
        "user_profile_picture": "elisha.jpg",
        "user_signup_date": "October 2016",
        "user_cover_image": "landscape1.jpg"
    },
     "b6d1f3b1-c6e8-46f0-892f-19fd065cbfal": {
        "user_id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfal",
        "user_first_name": "c", 
        "user_last_name": "cc",
        "user_name": "ElishaNgoma",
        "user_email": "s@s.com", 
        "user_password": "123",
        "user_profile_picture": "elisha.jpg",
        "user_signup_date": "October 2016",
        "user_cover_image": "landscape1.jpg"
    },
}


ADMIN = {
    "admin_id": "4e3c619b-1de5-45f5-8790-6871b8e67144",
    "admin_name": "Elisha",
    "admin_email": "admin@admin.com",
    "admin_password": "111"
}

######################## TWEETS ###############################

TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 500

now = datetime.now()
TWEET_TIME = now.strftime('%b %d. %H:%M')

TWEETS= {
    "baa13631-2b37-4e3d-b86c-5be1beea0217" : {
        "tweet_id": "baa13631-2b37-4e3d-b86c-5be1beea0217",
        "user_id":"a5ea9d0c-1295-4a1e-8184-e22e50ec1914",
        "user_first_name": "Aicha",
        "user_last_name": "Haidara",
        "user_name": "AichaHaidara",
        "user_profile_picture": "aicha.jpeg", 
        "tweet_text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work",
        "tweet_image": "cocker.jpeg",
        "tweet_time": "Jan 04. 17.15",
    }, 
    "cadbbcd7-b569-488c-adbe-adbf4c92b56a": {
        "tweet_id": "cadbbcd7-b569-488c-adbe-adbf4c92b56a",
        "user_id":"b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6", 
        "user_first_name": "Elisha", 
        "user_last_name": "Ngoma",
        "user_name": "ElishaNgoma",
        "user_profile_picture": "elisha.jpg",
        "tweet_text": "Last year has been the best year for manufacturing jobs and trucking jobs since 1994.",
        "tweet_image": "elisha.jpg",
        "tweet_time": "Mar 29. 20.30",
    },
    "9bbf2704-8377-4981-8b5d-db4ac9062042": {
        "tweet_id": "9bbf2704-8377-4981-8b5d-db4ac9062042",
        "user_id":"b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6", 
        "user_first_name": "Elisha", 
        "user_last_name": "Ngoma",
        "user_name": "ElishaNgoma",
        "user_profile_picture": "elisha.jpg",
        "tweet_text": "Adds htmlString in 4 positions see demo. Unlike .innerHTML it never rerenders and destroys the original HTML and references. The only thing.",
        "tweet_image": "dog.jpg",
        "tweet_time": "Feb 05. 12.01",
    },
}

######################## ICONS ###############################

items = [
  {"img":"elisha.jpg", "title":"BBC News", "user_name":"bbcworld"},
  {"img":"dalmatian.jpeg", "title":"Joe Biden", "user_name":"joebiden"},
  {"img":"elisha.jpg", "title":"Vice President", "user_name":"vp"},
  {"img":"elisha.jpg", "title":"Vice President", "user_name":"vp"},
]

tabs = [
  {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home",},
  {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
  {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
  {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
  {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
  {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
  {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
  {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
]

trends = [
  {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
  {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k"},
]