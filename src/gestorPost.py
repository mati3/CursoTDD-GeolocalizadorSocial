#!/usr/bin/env python
# coding: utf-8

from post import Post
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

class gestorPost:
    
    def __init__ (self, data):
        with open("../data/" + data) as file:
            # De momento tomaremos los post desde json de ejemplo. Posteriormente
            # estos datos se tomaran usando las API reales de las redes sociales
            self.posts = json.load(file)

    def getPosts(self):
        return self.posts

    def getPost(self, id):
        post = None
        for i in range(0, len(self.posts)):
            if self.posts[i]['_id'] == id:
                post = self.posts[i]
        return post

    def insertarPost(self, p):
        # Insertar post en la BD
        self.posts.append(p)

    def eliminarPost(self, p):
        # Borrar post de la BD
        self.posts.remove(p)

    def printPosts(self):
        for i in self.posts:
            print(i)
'''
if __name__=="__main__":
    gestorPost = gestorPost("posts.json")
    gestorPost.printPosts()
    posts = gestorPost.getPosts()
    print (posts[0])
    print (posts[0]['_id'])
    post_buscado = gestorPost.getPost("213123123")
    print ("Post buscado-> " + "Social: " + post_buscado['social'])
'''