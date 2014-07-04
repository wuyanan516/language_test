import urllib2
import cookielib

#name = 'goganan'
#password = '1qaz2wsx'

name = 'koichi'
password = 'password'

#url = 'https://www.hatena.ne.jp/login'
url = 'http://localhost/appfriends/admins'
req = urllib2.Request(url, 'data[User][username]=%s&data[User][password]=%s' % (name, password))
#req.add_header('hoge', 'fuga')

opener = urllib2.build_opener()
opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

conn = opener.open(req)

#url = 'http://d.hatena.ne.jp/%s/edit' % name
url = 'http://localhost/appfriends/admin_applications/csv_download/'
req = urllib2.Request(url)
conn = opener.open(req)

cont = conn.read()

data = cont.replace('\x0d\x0a', '\x0a')

f = open('out.csv', 'w')
f.write(data)
f.close()
