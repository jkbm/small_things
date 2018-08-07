##!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt
import requests
from bs4 import BeautifulSoup as BS
from yattag import Doc
import webbrowser
import os

def get_source():
	
	link = "http://www.skysports.com/transfer-centre"
	r = requests.get(link)
	soup = BS(r.content, "html.parser")

	sections = soup.find_all("section")
	
	return sections

def generate_html(search, news):
		#Generate HTML PAGE

	doc, tag, text = Doc().tagtext()
	with tag("h2"):
		text("Recent news for %s" % search)
	with tag('div', class_="news"):			    
		for n in news:
			with tag('p', id = "post"):
				text(n)

	result = doc.getvalue()

	return result

def get_news(search):
	sections = get_source()
	br = []
	for s in sections:
		p = s.find('p').stripped_strings
		ps = [x for x in p]
		t = ps[0] + "\n"
		t += " ".join(ps[1:])
		if search in t:
			br.append(t)

	br_lines = [x.replace("BREAKING NEWS", "BREAKING NEWS\n") for x in br]
	br_one = "\n".join(br_lines)
	html_text = generate_html(search, br_lines)
	
	
	if len(br) == 0:
		br_one = "No '%s' today." % search
		
	#Save txt
	with open(search + ".txt", "w") as f:
		f.write(br_one)
		f.close()
	
	#Save html
	filename = search + ".html"
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
	hf = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "base.html"), "r")	
	with open(filename, "w") as f:
		f.write(hf.read().replace("{{ block }}", html_text))
		hf.close()
		f.close()
	
	webbrowser.open_new(search+".html")

if __name__ == "__main__":
	args = sys.argv[1:]
	
	get_news(args[1])
	



