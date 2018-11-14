import time
import json
import requests
import urllib

def request_json(url, headers):
    s = requests.Session()
    if headers:
        s.headers.update(headers)
    return s.get(url).json()

def output_file(script_name, json_response):
    filename = 'output/%s_%s.json' % (script_name, time.strftime('%Y%m%d_%H%M_%S'))
    text_file = open(filename, "w")
    text_file.write(json.dumps(json_response, indent=2))
    text_file.close()
    print '==========='
    print 'output saved to %s' % filename
    print '==========='
    return
    
def get_airing_from_airing_id(airing_id):
    url_path = "http://watch.graph.api.espn.com/api?"
    apiKey = "d15c5790-7cb0-4fe1-8782-25f4698d0739"
    airing_query = "query%28%0A%20%20%24countryCode%3A%20String%21%2C%0A%20%20%24deviceType%3A%20DeviceType%21%2C%0A%20%20%24tz%3A%20String%2C%0A%20%20%24id%3A%20ID%21%0A%29%20%7B%0A%20%20airing%28%0A%20%20%20%20countryCode%3A%20%24countryCode%2C%0A%20%20%20%20deviceType%3A%20%24deviceType%2C%0A%20%20%20%20tz%3A%20%24tz%2C%0A%20%20%20%20id%3A%20%24id%0A%20%20%29%20%7B%20id%20name%20shortName%20description%20adobeRSS%20authTypes%20gameId%20requiresLinearPlayback%20type%20originalAiringStartDateTime%20startDateTime%20endDateTime%20duration%20source%20%7B%20url%20authorizationType%20hasEspnId3Heartbeats%20hasNielsenWatermarks%20hasPassThroughAds%20commercialReplacement%20startSessionUrl%20%7D%20network%20%7B%20id%20type%20name%20adobeResource%20%7D%20image%20%7B%20url%20%7D%20sport%20%7B%20name%20code%20uid%20%7D%20league%20%7B%20name%20uid%20%7D%20program%20%7B%20code%20%7D%20seekInSeconds%20simulcastAiringId%20airingId%20tracking%20%7B%20nielsenCrossId1%20trackingId%20%7D%20eventId%20packages%20%7B%20name%20%7D%20language%20tier%20feedName%20includeSponsor%20%7D%7D"
    airing_vars = "{\"id\":\"%s\",\"countryCode\":\"US\",\"deviceType\":\"SETTOP\",\"tz\":\"-8\"}" % airing_id
    url = (url_path+"apiKey="+apiKey+"&query="+airing_query+"&variables="+urllib.quote(airing_vars))
    return json.dumps(request_json(url, None), indent=2)    