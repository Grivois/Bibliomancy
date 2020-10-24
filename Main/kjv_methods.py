# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:43:11 2019

@author: Grivois
"""
from random import randint


class Biblework():
    def divination(self):
        with open("KJV_table1.txt", "r") as text_file:
            book = randint(1, 66)
            lines = text_file.readlines()
            x = lines[book]
            y = x.split()
            verseno = len(y)-2
            chapter = randint(1,(verseno)) + 1
            verse = randint(1,int(y[chapter]))
            locationname = y[1] +  ' ' + str(chapter - 1) + ':' + str(verse)
            location = str(book).zfill(2) +':' + str(chapter - 1).zfill(3)  + ':' + str(verse).zfill(3)
            weblocation = 'https://www.biblegateway.com/verse/en/' + y[1].replace('_','%20') + '%20' + str(chapter - 1) + ':' +str(verse)
            print('location: '+location)
            print('locationname: ' + locationname)
            return location,locationname,weblocation
            text_file.close()

        
    def interperter(self, location, locationname):
        with open('KJV.txt', 'r') as f:
            for line in f:
                if (location in line):
                    gospel = line
                    for line in f:
                        for w in range(9):
                            if ( str(w)  in line):
                                break
                        else:
                            gospel += line
                            continue
                        break
        gospel = locationname.replace('_',' ') +'\n'+ gospel.replace(location, '').replace('\n', ' ').replace('           ', '') 
        return gospel
        f.close()
        
    def logos(self):
        b = Biblework()
        g = b.divination()
        p = b.interperter(g[0], g[1])
        return p, g[2]
    
class Omega():
    b = Biblework()
    l = b.logos()
    word = l[0]
    web = l[1]
    
    
b = Biblework()
l = b.logos()
web = l[1]
word = l[0]
o = Omega()
print (o.word)
print (o.web)
#g = b.divination()
#p = b.interperter(g[0], g[1])
#x = b.divination()
#print(x)
#print(p)
#print(web)
#print(word)
