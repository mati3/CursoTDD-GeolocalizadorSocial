#!/usr/bin/env python
# coding: utf-8

import unittest
import json
import sys, os.path

src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/')
sys.path.append(src_path)

from post import Post
from gestorPost import GestorPost

sample_posts = [
    {
        "_id":"111222333",
        "social": "Twitter",
        "autor": "anon192",
        "tags": ["Debate", "Elecciones"],
        "location": "Granada"
    },
    {
        "_id":"123123123",
        "social": "Facebook",
        "autor": "anon892",
        "tags": ["Debate"],
        "location": "Barcelona"
    },
    {
        "_id":"999888777",
        "social": "Instagram",
        "autor": "anon784",
        "tags": ["Italia", "Pizza"],
        "location": "Roma"
    }
]

sample_post_id = {
    "_id":"111222333",
    "social": "Twitter",
    "autor": "anon192",
    "tags": ["Debate", "Elecciones"],
    "location": "Granada"
}

class TestPost(unittest.TestCase):

    # Comprueba que los post se crean correctamente
    def test_create_post(self):
        tags = ["test", "python"]
        p = Post("Federico", tags, "Twitter", "Granada")

        self.assertEqual(p.getAutor(),"Federico", "Autor devuelto incorrecto")
        self.assertEqual(p.getTags(), tags, "Tags devueltos incorrectos")
        self.assertEqual(p.getSocial(),"Twitter", "Red social devuelta incorrecta")
        self.assertEqual(p.getLocation(),"Granada", "Localizacion devuelta incorrecta")

    # Comprueba que la obtención de posts se realizan correctamente
    def test_get_posts(self):
        gestorPost = GestorPost("data/posts.json")
        self.assertEqual(gestorPost.getPosts(), sample_posts, "Posts devueltos correctamente")

    def test_get_post(self):
        gestorPost = GestorPost("data/posts.json")
        self.assertEqual(gestorPost.getPost("111222333"), sample_post_id, "Post devuelto correcto")
