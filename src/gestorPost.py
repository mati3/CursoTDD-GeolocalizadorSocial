#!/usr/bin/env python
# coding: utf-8

from post import Post

class gestorPost:
    
    def __init__ (self, p):
        self.posts = p
    
    def insertarPost(self, p):
        self.posts.append(p)

    def borrarPost(self, p):
        self.posts.remove(p)

    def 

    def print(self):
        with open(.json) as file:
            data = json.load(file)
        for i in self.posts
            print(i)


