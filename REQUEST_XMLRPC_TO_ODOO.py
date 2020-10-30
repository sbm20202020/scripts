import functools
import xmlrpc.client

HOST = 'localhost'
PORT = 8069
DB = 'openacademy'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,'admin',PASS)
print("Logged in as %s (uid: %d)" % ('admin', uid))

call = functools.partial(xmlrpc.client.ServerProxy(ROOT + 'object').execute,DB, uid, PASS)

sessions = call('openacademy.session','search_read', [], ['id','name','seats'])

for session in sessions:
    print("Session [ %s ] - [ %s ] - (%s Places)" % (session['id'],session['name'], session['seats']))

   
# 3.create a new session   
# courses = call('openacademy.course','search_read',[],['id'])
# for cours in courses:
#     if (cours['id']==1):
#         session_id = call('openacademy.session', 'create', {
#             'name' : 'Homme RPC 2020',
#             'cours_id' : 1,
#         })
        
# 3.create a new session for the "Functional" course
course_id = call('openacademy.course', 'search', [('name','ilike','DJANGO 2.3')])[0]
session_id = call('openacademy.session', 'create', {
    'name' : 'CIGA YEBELA',
    'cours_id' : course_id,
})