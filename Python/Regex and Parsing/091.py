# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print("-> {} > {}".format(*attr)) for attr in attrs]
        
html = "\n".join([input() for i in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()