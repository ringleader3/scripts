import json_helper
import argparse
import espn_endpoints

parser = argparse.ArgumentParser()
parser.add_argument("--token", help="dss session token", type=str)
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
    
resp_json = json_helper.request_json(request_url, {'dss-session-token': args.token} if args.token else None)

for bucket in resp_json['page']['buckets']:
    print "====="
    print "Bucket: %s" % bucket['name']
    for content in bucket['contents']:
        print "Name: %s" % content['name']
        print "ID: %s" % content['id']
        
exit()