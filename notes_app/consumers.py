import json
from channels.channel import Group


def ws_connect(message):
    message.reply_channel.send({"accept": True})
<<<<<<< HEAD
    Group('request_stat').add(message.reply_channel)
    print 'CONNECTION created'
    print
    
    
=======
    Group('chat').add(message.reply_channel)


>>>>>>> t10_db_requests_page_async
def ws_message(message):
    # retrieving data to be displayed
    from notes_app.models import RequestStat
    requests = RequestStat.objects.all().order_by('-id')[:10]
    new_req_num = len(RequestStat.objects.filter(is_new=True))
    req_stat = [str(k) for k in requests]
    RequestStat.objects.filter(is_new=True).update(is_new=False)
<<<<<<< HEAD
    for a in req_stat:
        print a
    print
    Group('request_stat').send({'text': json.dumps({'new_req_num': new_req_num, 
=======
    # sending 'message'
    Group('chat').send({'text': json.dumps({'new_req_num': new_req_num,
>>>>>>> t10_db_requests_page_async
                                            'req_stat': req_stat,
                                            'req_page_path': message.content['text']})
                        })


def ws_disconnect(message):
<<<<<<< HEAD
    Group('request_stat').discard(message.reply_channel)
    print 'DISCONNECTED'
    for k,v in message.content.iteritems():
    	print k,": ",v
    print
=======
    Group('chat').discard(message.reply_channel)
>>>>>>> t10_db_requests_page_async
