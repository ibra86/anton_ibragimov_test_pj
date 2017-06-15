import json
from channels.channel import Group


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('chat').add(message.reply_channel)


def ws_message(message):
    # retrieving data to be displayed
    from notes_app.models import RequestStat
    requests = RequestStat.objects.all().order_by('-id')[:10]
    new_req_num = len(RequestStat.objects.filter(is_new=True))
    req_stat = [str(k) for k in requests]
    RequestStat.objects.filter(is_new=True).update(is_new=False)
    # sending 'message'
    Group('chat').send({'text': json.dumps({'new_req_num': new_req_num,
                                            'req_stat': req_stat,
                                            'req_page_path': message.content['text']})
                        })


def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
