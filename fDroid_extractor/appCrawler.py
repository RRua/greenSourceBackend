import sys
import json
import os,fnmatch
from pprint import pprint
from subprocess import call, check_output, Popen, PIPE



def createDir(dirname, content):
    try:
        os.mkdir(dirname)
        with open(dirname+"/data.json", 'w') as outfile:
            json.dump(content, outfile)
        print("ja taaa")
    except Exception as e:
        print ("Creation of the directory %s failed" % dirname)


def downloadSauce(obje):
    dirname = "./fdroidApps/" + str(obje['url']).replace("https://f-droid.org/repo/","") 
    cmd =' curl ' + obje['url'] + ' --output ' + dirname+"/"+ str(obje['url']).replace("https://f-droid.org/repo/","") 
    #.replace(".tar.gz","")
    createDir(dirname,obje)
    pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    std_out, std_err = pipes.communicate()
    pipes.wait()
    if pipes.returncode != 0:
        # an error happened!
        err_msg = "{}. Code: {}".format(std_err.decode("UTF-8"), pipes.returncode)
        print(err_msg)
    else:
        print("ok")


def getSauce(url):
    cmd ='scrapy runspider sourceCodeCrawler.py -a url=\"' +url  + '\" -s LOG_ENABLED=False -o  batata.json'
    #process = Popen(cmd,shell=True, stdout=PIPE)
    pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    std_out, std_err = pipes.communicate()
    pipes.wait()
    if pipes.returncode != 0:
        # an error happened!
        err_msg = "{}. Code: {}".format(std_err.decode("UTF-8"), pipes.returncode)
        print(err_msg)
    else:
        print("ok")


def getAppPageFromListPage(url):
    cmd ='scrapy runspider appListCrawler.py -a url=\"' +url  + '\" -s LOG_ENABLED=False -o  pages.json'
    #process = Popen(cmd,shell=True, stdout=PIPE)
    pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    std_out, std_err = pipes.communicate()
    pipes.wait()
    if pipes.returncode != 0:
        # an error happened!
        err_msg = "{}. Code: {}".format(std_err.decode("UTF-8"), pipes.returncode)
        print(err_msg)
    else:
        print("ok")


def main(args):
    top_url = "https://f-droid.org/pt_BR/packages/"
    numpages = 67
    start_index = 2
    #one_app_url = "https://f-droid.org/pt_BR/packages/com.uberspot.a2048/"
    #getSauce(one_app_url)
    #for x in range(start_index,numpages):
        #new_list_url = ( "https://f-droid.org/pt_BR/packages/%i/index.html" % x)
        #getAppPageFromListPage(new_list_url)
        #print("page %i processed..." %x )

    #with open('pages.json') as json_file:
    #    data = json.load(json_file)
    #for x in data.values():
    #    for url in x:
    #        real_url = "https://f-droid.org" + url
    #        getSauce(real_url)
    #        print("processed " + real_url)
    with open('batata.json') as json_file:
        data = json.load(json_file)
    #print(len(data))
    ct = len(data)
    for x in data:
        ct=ct-1
        print(x['url'])
        downloadSauce(x)
        print("Downloading apk " + str(ct))




if __name__ == "__main__":
   main(sys.argv[1:])
