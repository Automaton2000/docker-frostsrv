import os
from lxml import etree as et

tree = et.parse('FROST-Server.xml')

element = tree.find('//Resource')
element.set('username', os.environ['postgres_user'])
element.set('password', os.environ['postgres_pw'])
element.set('url', 'jdbc:postgresql://'+os.environ['postgres_url']+':'+os.environ['postgres_port']+'/'+os.environ['postgres_db_name'])
#print('Current value is:', element.get('username'))

with open('./FROST-Server.xml', 'wb') as f:
    f.write(et.tostring(tree))

#print(et.tostring(tree))


