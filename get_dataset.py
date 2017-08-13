import requests
import string
from html.parser import HTMLParser
from io import open as iopen
import os

if not os.path.exists('db'):
    os.makedirs('db')


article_list = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global article_list
        if tag == "article":
            for attr in attrs:
                if attr[0] == 'data-articlecode':
                    article_list.append(attr[1])
        #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        return

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        return

image_list = []
class MyHTMLParser1(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global image_list
        if tag == "img":
            for attr in attrs:
                if attr[0] == 'class' and "product-detail-thumbnail" in attr[1]:
                    for attr2 in attrs:
                        if attr2[0] == 'src':
                            image_list.append(((attr2[1][2:]).replace("thumb","zoom")+"&zoom=zoom"))
                            #print(attr2)
        #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        return

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        return

def save_image(file_url,file_save):
    i = requests.get(file_url)
    if i.status_code == requests.codes.ok:
        with iopen(file_save, 'wb') as file:
            file.write(i.content)
    else:
        return False

parser = MyHTMLParser()
parser1 = MyHTMLParser1()

base_url = "http://www2.hm.com/"

article_url = "/fr_fr/productpage."

to_mine_type = ["robes"]
to_mine_url = ["fr_fr/femme/catalogue-par-produit/robes.html?product-type=ladies_dresses&image=model&sort=stock&offset=0&page-size=400"]

for t in to_mine_type:
    if not os.path.exists('db/'+str(t)):
        os.makedirs('db/'+t+'/cat')
        os.makedirs('db/'+t+'/mod')

for (i,t) in enumerate(to_mine_type):
    print("Mining "+t+"...")
    good_url = base_url+to_mine_url[i]
    print("Downloading "+good_url+"...")
    r = requests.get(good_url)
    htmlSource = r.text
    print("Parser html to get product list...")
    article_list = []
    parser.feed(htmlSource)
    print(str(len(article_list))+" articles found in the category "+t+"...")
    for (i_article,article) in enumerate(article_list):
        print("Getting "+t+" "+str(i_article)+"/"+str(len(article_list)))
        image_list = []
        that_article_url = base_url+article_url+article+".html"
        r = requests.get(that_article_url)
        parser1.feed(r.text)
        save_image("http://"+image_list[0],"db/"+t+"/mod/"+str(i_article)+".jpg")
        for (j,img) in enumerate(image_list[1:]):
            save_image("http://"+img,"db/"+t+"/cat/"+str(i_article)+"_"+str(j)+".jpg")