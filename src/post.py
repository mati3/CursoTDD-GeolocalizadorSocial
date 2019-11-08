#!/usr/bin/env python
# coding: utf-8

class Post:
    
    def __init__ (self, autor, tags, social, location):
        self.autor = autor
        self.tags = tags
        self.social = social
        self.location = location
        
    def getAutor(self):
        return self.autor
    
    def getTags(self):
        return self.tags
    
    def getSocial(self):
        return self.social
    
    def getLocation(self):
        return self.location  
