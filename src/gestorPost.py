#!/usr/bin/env python
# coding: utf-8

from post import Post
import json
import sys, os.path

class GestorPost:
    
    def __init__ (self, data_path):

        with open(data_path) as file:
            # Obtener datos desde un fichero de ejemplo .json
            self.posts = json.load(file)

    def getPosts(self):
        return self.posts

    def getPost(self, id):
        post = None
        for i in range(0, len(self.posts)):
            if self.posts[i]['_id'] == id:
                post = self.posts[i]
        return post

    def printPosts(self):
        for i in self.posts:
            print(i)
