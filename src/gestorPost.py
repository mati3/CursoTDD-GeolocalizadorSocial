#!/usr/bin/env python
# coding: utf-8

from post import Post

class gestorPost:
    
    def __init__ (self, p):
        self.posts = p
    
    def insertarPost(self, p):
        self.posts.append(p)

    def borrarPost(p):
        self.posts.remove(p)


