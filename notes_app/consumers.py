import json
from channels.channel import Group

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('chat').add(message.reply_channel)
    print 'CONNECTION created'
    print
    
    
def ws_message(message):
    print 'MESSAGE sent'
    for k,v in message.content.iteritems():
    	print k,": ",v
    print 'STATS'
    from notes_app.models import RequestStat
    requests = RequestStat.objects.all().order_by('-id')[:10]
    new_req_num = len(RequestStat.objects.filter(is_new=True))
    req_stat = [str(k) for k in requests]
    RequestStat.objects.filter(is_new=True).update(is_new=False)
    for a in req_stat:
        print a
    print
    Group('chat').send({'text': json.dumps({'new_req_num': new_req_num, 
                                            'req_stat': req_stat,
                                            'req_page_path': message.content['text']})
                                            });
#     Group('chat').discard(message.reply_channel)
    
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
    print 'DISCONNECTED'
    for k,v in message.content.iteritems():
    	print k,": ",v
    print