##!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Samuel Guebo,Paul Bouaffou
# Description: Utility file
# License: MIT
#
#
import os
from tinydb import TinyDB


def getDb():
	""" Return a Database (TinyDB) object """
	dbFolder = "database"
	if not os.path.exists(dbFolder):
		os.makedirs(dbFolder)

	db = TinyDB(dbFolder + '/db.json')
	return db


def getArticles(limit=10):
	""" Return all articles in the database """ 
	db = getDb()
	results = db.all()

	if len(results) < limit:
		return results[0:limit-1]
	
	return results


def createArticle(article):
	""" Insert new article database """ 
	db = getDb()
	return db.insert(article)


def printNotice(notice):
	"""Print notice message in yellow """
	print('\033[93m' + notice + '\033[0m')