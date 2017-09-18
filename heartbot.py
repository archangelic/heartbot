from pprint import pprint
import random

import ananas
import emoji

hearts = [
    ':heart:',
    ':blue_heart:',
    ':yellow_heart:',
    ':purple_heart:',
    ':green_heart:',
    ':heartbeat:',
    ':heartpulse:',
    ':two_hearts:',
    ':revolving_hearts:',
    ':cupid:',
    ':sparkling_heart:',
]

class HeartBot(ananas.PineappleBot):
    @ananas.reply
    def post_hearts(self, status, user):
        mentions = [i for i in status['mentions'] if i['acct'] != 'hearts']
        message = ''
        for i in range(0, 10):
            message += ' ' + random.choice(hearts)
        message = emoji.emojize(message.replace(' ', ''), use_aliases=True)
        for m in mentions:
            message = '@{} {}'.format(m['acct'], message)
        message = '@{} {}'.format(status['account']['acct'], message)
        if status['spoiler_text']:
            spoiler = status['spoiler_text']
        else:
            spoiler = None
        if status['in_reply_to_id']:
            reply_to = status['in_reply_to_id']
        else:
            reply_to = status['id']
        self.mastodon.status_post(
            status=message,
            in_reply_to_id=reply_to,
            spoiler_text=spoiler
        )


