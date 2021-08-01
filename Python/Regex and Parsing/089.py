# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print("Start :",tag)
        for element in attributes:
            print("->",element[0], ">", element[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attributes):
        print("Empty :", tag)
        for element in attributes:
            print("->",element[0],">",element[1])

MyParser = MyHTMLParser()
MyParser.feed("".join([input().strip() for i in range(int(input()))]))
        
            
                