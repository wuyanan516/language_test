import urllib2
import cookielib

#name = 'goganan'
#password = '1qaz2wsx'

name = 'applezzx@silicon-breath.jp'
password = 'password'

#url = 'https://www.hatena.ne.jp/login'
url = 'http://localhost/appfriends/mypage/login'
req = urllib2.Request(url, '_method=POST&data[User][email]=%s&data[User][password]=%s' % (name, password))
#req = urllib2.Request(url, '_method=POST&data%5BUser%5D%5Bemail%5D=applezzx%40silicon-breath.jp&data%5BUser%5D%5Bpassword%5D=password&x=119&y=18'
#req.add_header('hoge', 'fuga')

opener = urllib2.build_opener()
opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

conn = opener.open(req)

#url = 'http://d.hatena.ne.jp/%s/edit' % name

url = 'http://localhost/appfriends/mypage_userinfo'
req = urllib2.Request(url)
conn = opener.open(req)

cont = conn.read()

f = open('out_top.html', 'w')
f.write(cont)
f.close()
