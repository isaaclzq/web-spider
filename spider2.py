import urllib

con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
title = con.find(r'<a title=')
count = 0
total_link = 7
cur_link = 1
while cur_link <= total_link:
	title = con.find(r'<a title=')
	while title != -1:
		href = con.find(r'href=', title)
		html = con.find(r'.html', href)
		url = con[href + 6: html + 5]
		filename = url[url.find(r'blog_'):url.find(r'html')+ 4]
		files = urllib.urlopen(url).read()
		open(filename, 'w').write(files)
		title = con.find(r'<a title=', html)
		count += 1
		print 'Case ' + str(count) + ' finished'
	cur_link += 1
	con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(cur_link) + '.html').read()
print 'all finished'

