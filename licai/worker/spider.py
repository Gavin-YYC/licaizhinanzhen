# coding=utf-8

import urllib2
import urllib

class Spider( object ):

    def _init__( self ):
        pass

    def get_data ( self, url, payload=None, mobild=False ):

        if mobild:
            user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        else:
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

        headers = {
            'User-agent': user_agent
        }
        request = urllib2.Request( url, headers=headers )
        if payload is None:
            response = urllib2.urlopen( request )
        else:
            response = urllib2.urlopen( request, urllib.urlencode(payload) )
        resp = response.read()
        return resp
