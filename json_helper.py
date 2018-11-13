import time
import json
import requests

def request_json(url, token):
    s = requests.Session()
    s.headers.update({'dss-session-token': token})
    return s.get(url).json()

def output_file(json_file):
    filename = 'output/output_rec_rows_%s.json' % time.strftime('%Y%m%d_%H%M_%S')
    text_file = open(filename, "w")
    text_file.write(json.dumps(json_file, indent=2))
    text_file.close()
    print '==========='
    print 'output saved to %s' % filename
    print '==========='
    return