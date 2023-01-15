import requests as rq

url = 'https://www.casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/'
user = 'pabloemma'
pwd = '?Pa!blo?nuke'


file = 'iperf.log'
r = rq.get(url+file, auth=(user,pwd))
filename = 'requests1.txt'

if r.status_code == 200:
    with open(filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if(chunk):
                f.write(chunk)

f.close()
user = 'pabloemma'
pwd = '?Pa!blo?nuke'

combo1 = user+':'+pwd

import subprocess
#command = 'curl --user "\"pabloemma:?Pa!blo?nuke\"" -T /Users/klein/login.txt https://casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/Temperature/'
command = 'curl --user '+combo1+' -T /Users/klein/login.txt https://casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/Temperature/'
subprocess.Popen(command,shell=True)


myurl = 'https://casitadongaspar.com/nextcloud/Temperature/'
# now lets try to put a file on nextcloud
upfile = {'file':open('/Users/klein/login.txt','rb')}
#with open('/Users/klein/finnland.pdf','rb') as f:
r = rq.post(myurl,files=upfile, auth=(user,pwd))

print('r')
r.text
#r = rq.post(url,files=upfile)


print(r.status_code)