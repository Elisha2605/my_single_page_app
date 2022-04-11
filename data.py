######################## REGEX ###############################
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

######################## UUID ###############################
REGEX_UUID4 = '^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'

######################## SESSIONS ###############################
SESSIONS = []
COOKIE_SECRET = "Tis is my secret"

######################## USERS ###############################

USERS = {
    "a5ea9d0c-1295-4a1e-8184-e22e50ec1914": {
        "user_id": "a5ea9d0c-1295-4a1e-8184-e22e50ec1914",
        "user_first_name": "Aicha",
        "user_last_name": "Haidara",
        "user_name": "AichaHaidara",
        "user_email": "a@a.com", 
        "user_password": "123",
        "user_profile_picture": "dalmatian.jpeg",
    },
    "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6": {
        "user_id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6",
        "user_first_name": "Elisha", 
        "user_last_name": "Ngoma",
        "user_name": "ElishaNgoma",
        "user_email": "elisha_ngoma@yahoo.fr", 
        "user_password": "123",
        "user_profile_picture": "elisha.jpg",
    },
}

ADMIN = {
    "admin_email": "admin@admin.com",
    "admin_password": "111"
}

######################## TWEETS ###############################

TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 500



TWEETS= {
    "baa13631-2b37-4e3d-b86c-5be1beea0217" : {
        "tweet_id": "baa13631-2b37-4e3d-b86c-5be1beea0217",
        "user_id":"a5ea9d0c-1295-4a1e-8184-e22e50ec1914",
        "user_first_name": "Aicha",
        "user_last_name": "Haidara",
        "user_name": "AichaHaidara",
        "user_profile_picture": "dalmatian.jpeg", 
        "tweet_text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work",
        "tweet_image": "cocker.jpeg",
        "tweet_date": "",
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
        "tweet_date": "",
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
        "tweet_date": "",
    },
}



######################## ICONS ###############################

tweets = [
  {"id":"1", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"2", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"3", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"id":"4", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"5", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"6", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"id":"7", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"8", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"9", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"id":"10", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"11", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"12", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
]

items = [
  {"img":"bbc.png", "title":"BBC News", "user_name":"bbcworld"},
  {"img":"biden.jpg", "title":"Joe Biden", "user_name":"joebiden"},
  {"img":"harris.jpg", "title":"Vice President", "user_name":"vp"},
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

people = [
  {"src": "stephie.png", "name": "Stephie Jensen", "handle": "@sjensen"},
  {"src": "monk.jpg", "name": "Adrian Monk", "handle": "@detective :)"},
  {"src": "kevin.jpg", "name": "Kevin Hart", "handle": "@miniRock"}
]

trends = [
  {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
  {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k"},
  {"category": "Russia", "title": "Russia", "tweets_counter": "10k"},
]