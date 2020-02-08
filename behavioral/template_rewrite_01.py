#!/usr/bin/env python
# -*- coding: utf-8 -*-

templates = [(g, a, s)
             for g in ('a', 'b')
             for a in ('c', 'd')
             for s in ('e', 'f')]

print(templates)
"""
[
('a', 'c', 'e'), 
('a', 'c', 'f'), 
('a', 'd', 'e'), 
('a', 'd', 'f'), 
('b', 'c', 'e'), 
('b', 'c', 'f'), 
('b', 'd', 'e'), 
('b', 'd', 'f')
]
"""
