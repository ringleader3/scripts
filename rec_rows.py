#!/usr/local/bin/python
import argparse
import espn_endpoints
import json_helper
import os

parser = argparse.ArgumentParser()
parser.add_argument("--token", help="dss session token", type=str, default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb250ZXh0Ijp7InByb2ZpbGVzIjpbeyJhY3RpdmUiOnRydWUsInR5cGUiOiJ1cm46YmFtdGVjaDpwcm9maWxlIiwiaWQiOiJ1c2VyXzEiLCJwYXJlbnRhbF9jb250cm9scyI6eyJlbmFibGVkIjpmYWxzZX19XX19.D-oSieYZYy58YZBMv_lSm_i0-LR1zqSCNK3r1XRl7V8")
parser.add_argument("--url", help="optional url - this overrides the endpoint option", type=str)
parser.add_argument("--endpoint", help="choose a platform for the pageAPI endpoint", choices=espn_endpoints.endpoints.keys())
args = parser.parse_args()

if args.url:
    request_url = args.url
elif args.endpoint:
    request_url = espn_endpoints.endpoints[args.endpoint]
else:
    print 'either add provide a url or choose an endpoint, please run with -h for help'
    exit()

print '==========='
print 'SAMPLE CURL:'    
print 'curl -H \"dss-session-token:%s\" \"%s\"' % (args.token, request_url)
print '==========='

resp_json = json_helper.request_json(request_url, {'dss-session-token': args.token})

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

json_helper.output_file(os.path.basename(__file__), resp_json)

exit()