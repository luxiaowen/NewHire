import urllib
def checkurl(weburl):
    doc = urllib.urlopen(weburl)
    #print doc.getcode()
    return doc.getcode()==404
