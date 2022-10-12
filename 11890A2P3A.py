#!/usr/bin/env python
"""Scrape a webpage for documents

This bare minimum implementation is a Proof of Concept only.
"""
import argparse
import html.parser
import urllib.request

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.files = []
    # Override how to handle the start tag of an element.
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag that contains '.'.
        if tag == "a":
           for name,link in attrs:
               if name == "href" and '.' in link:
                   self.files.append(link)

def main(arg):
    url = arg.url   # TODO: validate url (http://255.255.255.255/)
    targets = []
    try:
        with urllib.request.urlopen(arg.url) as f:
            a = MyHTMLParser()
            a.feed(f.read().decode('utf-8'))
            targets = a.files
    except Exception as e:
        print(e)
    if targets:
        for i in targets:
            urllib.request.urlretrieve(url + i, i)
            print(f'{i} fetched')
    else:
        print('Nothing to fetch')

if __name__	== '__main__':
    parser = argparse.ArgumentParser(prog='crawl_web',
                                     description='A web crawler')
    parser.add_argument('url')
    main(parser.parse_args())
