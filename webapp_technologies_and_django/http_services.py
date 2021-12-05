from urllib import request, parse

url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

parms = {
'name1' : 'value1',
'name2' : 'value2'
}

def simple_get_request(parms,url):
    querystring = parse.urlencode(parms) #'name1=value1&name2=value2'
    u = request.urlopen(url+'?' + querystring)
    resp = u.read()
    return resp

print(simple_get_request(
    parms,url_get
))