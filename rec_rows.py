#!/usr/local/bin/python
import requests
import json
import time
import argparse
import espn_endpoints

parser = argparse.ArgumentParser()
parser.add_argument("--token", help="dss session token", type=str, default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb250ZXh0Ijp7InByb2ZpbGVzIjpbeyJhY3RpdmUiOnRydWUsInR5cGUiOiJ1cm46YmFtdGVjaDpwcm9maWxlIiwiaWQiOiJ1c2VyXzEiLCJwYXJlbnRhbF9jb250cm9scyI6eyJlbmFibGVkIjpmYWxzZX19XX19.D-oSieYZYy58YZBMv_lSm_i0-LR1zqSCNK3r1XRl7V8")
parser.add_argument("--url", help="optional url - this overrides the endpoint option", type=str)
parser.add_argument("--endpoint", help="choose a platform for the pageAPI endpoint", choices=espn_endpoints.endpoints.keys())
args = parser.parse_args()

if args.url:
    url = args.url
elif args.endpoint:
    url = espn_endpoints.endpoints[args.endpoint]
else:
    print 'either add provide a url or choose an endpoint, please run with -h for help'
    exit()

print '==========='
print 'SAMPLE CURL:'    
print 'curl -H \"dss-session-token:%s\" \"%s\"' % (args.token, url)
print '==========='

s = requests.Session()
s.headers.update({'dss-session-token': args.token})
resp_json = s.get(url).json()

print 'Recommended for You content:'
rec_buckets = int(0)
for bucket in resp_json['page']['buckets']:
    if bucket['name'] == 'Recommended for You':
        for content in bucket['contents']:
            print content['name']
            print content['streams'][0]['dss']
        rec_buckets += 1

if rec_buckets == 0:
    print 'No Recommended for You row found'

filename = 'output/output_rec_rows_%s.json' % time.strftime('%Y%m%d_%H%M_%S')
text_file = open(filename, "w")
text_file.write(json.dumps(resp_json, indent=2))
text_file.close()

print '==========='
print 'output saved to %s' % filename
print '==========='
exit()