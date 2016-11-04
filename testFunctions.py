from utils import newStory, auth, addUpdate, posts

user = "user1"
title = "title1"
text = "text1 lkajsbfklajsbfajklsdbfksdjkbfaklsjbfaskjbflajbfklajsbfasjklbfa"

newStory.addStory(user,title,text)


user = "user1"
title = "title2"
text = "text2 akljsdbfakljsdbfakljsdbfaklsjdbfakljsdbfakljsdbfaklsjbfasdfasd"

newStory.addStory(user,title,text)

user = "user2"
title = "title3"
text = "text3 klajsfakljsdbfakljsdbfakljsdbfklajdsdbfaklsjdbfaskldbfasjkldbf"

newStory.addStory(user,title,text)

posts.getFeed("user1")
'''
text = "New moon.w hat the time"

addUpdate.newUpdate(1,user,text)

text = "asdfghjkl"
user = "456"

addUpdate.newUpdate(1,user,text)

'''
