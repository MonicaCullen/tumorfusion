f = open('/home/wul/project/platform/app/tumorfusion/templates/test.txt')

dis = set()
for line in f:
	data = [i.strip() for i in line.split('|') if i.strip()]
	dis.update(data)

print len(dis)