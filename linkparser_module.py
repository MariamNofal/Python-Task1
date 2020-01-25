import requests
from bs4  import BeautifulSoup, Comment
import lxml
import tldextract
from arg_pars import parse_arg
import sys

def run(args):
		farg, link= parse_arg(args)
		if farg is not None:
			sys.stdout = open(farg, 'w')
		if (link is None) or (link ==""):
			help()
			return
		print(link)
		print("*****TAGS*****")
		_get_all_tags(link)
		print("*****COMMENTS******")
		_get_comments(link)
		print("*****URLs******")
		_get_urls(link)
		print("*****DOMAINS******")
		_get_domains(link)
		print("*****SUBDOMAINS******")
		_get_subdomains(link)
		sys.stdout = sys.__stdout__
	

def help():
	print("HELP PAGE")
	print("enter valid http request ex. https://google.com")

	



def _soup(link):

	try:
		responce = requests.get(link)
		data = responce.content
		soup = BeautifulSoup(data, 'html.parser')
		return soup
	except requests.exceptions.ConnectionError :
		print("Failed to establish a new connection or service not known")
	except:
		print("entervalid http request ex. https://google.com")

def _get_all_tags(link):
	unique_tags =list(set(tag.name for tag in _soup(link).find_all()))
	print(unique_tags)


def _get_comments(link):
	comments=  _soup(link).find_all(string=lambda text: isinstance(text, Comment))
	for c in comments:
	    print(c)
	    print("===========")
	    c.extract()

def _get_urls(link):
		links = _soup(link).find_all('a')
		for i in links:
			url=i.get('href') 
			print(url)
			
def _get_domains(link):
	links = _soup(link).find_all('a')
	for i in links:
		url=i.get('href') 
		extracted = tldextract.extract(url)
		print("{}.{}".format(extracted.domain, extracted.suffix))
def _get_subdomains(link):
	links = _soup(link).find_all('a')
	for i in links:
		url=i.get('href') 
		extracted = tldextract.extract(url)
		print("{}".format(extracted.subdomain))
