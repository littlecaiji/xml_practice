# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET

updateTree = ET.parse('movies.xml')
root = updateTree.getroot()

for movie in root.findall('book'):
    for author in movie.findall('author'):
        author.text = "cjh"


updateTree.write("movies.xml")