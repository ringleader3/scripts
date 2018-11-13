import time
import json
import requests

def request_json(url, headers):
    s = requests.Session()
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