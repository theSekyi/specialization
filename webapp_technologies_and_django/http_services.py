from urllib import request, parse

url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

parms = {
'name1' : 'value1',
'name2' : 'value2'
}

headers = {
'User-agent' : 'none/ofyourbusiness',
'Spam' : 'Eggs'
}

def simple_get_request(parms,url):
    querystring = parse.urlencode(parms) #'name1=value1&name2=value2'
    u = request.urlopen(url+'?' + querystring)
    resp = u.read()
    return resp

def simple_post_request(parms,url):
    querystring = parse.urlencode(parms) #'name1=value1&name2=value2'
    u = request.urlopen(url+'?' + querystring.encode('ascii'))
    resp = u.read()
    return resp

def simple_request_with_headers(parms,headers,url):
    querystring = parse.urlencode(parms)
    req = request.Request(url, querystring.encode('ascii'), headers=headers)
    u = request.urlopen(req)
    resp = u.read()
    return resp