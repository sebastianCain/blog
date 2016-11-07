from utils import newStory, auth, addUpdate, posts

user = "user1"
title = "title1"
text = "text1"

newStory.addStory(user,title,text)


user = "user1"
title = "title2"
text = "text2"

newStory.addStory(user,title,text)

user = "user1"
title = "title3"
text = "text3"

newStory.addStory(user,title,text)

user = "user2"
title = "title4"
text = "text4"

newStory.addStory(user,title,text)


addUpdate.newUpdate(3, "user3", "update1")
addUpdate.newUpdate(3, "user2", "update2")
addUpdate.newUpdate(4, "user4", "update1")


#posts.getFeedData("user1")
posts.getContributedData("user2")
4
