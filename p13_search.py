import requests
import json
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--token", help="dss session token", type=str, default="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb250ZXh0Ijp7InByb2ZpbGVzIjpbeyJhY3RpdmUiOnRydWUsInR5cGUiOiJ1cm46YmFtdGVjaDpwcm9maWxlIiwiaWQiOiJ1c2VyXzEiLCJwYXJlbnRhbF9jb250cm9scyI6eyJlbmFibGVkIjpmYWxzZX19XX19.D-oSieYZYy58YZBMv_lSm_i0-LR1zqSCNK3r1XRl7V8")
parser.add_argument("--swid", help="swid", type=str, default="605C124C-EB99-40FC-9643-32D571A911DE")
parser.add_argument("--url", help="url", type=str, default="https://search-api-qa.svcs.plus.espn.com/svc/search/v2/graphql/persisted/query/espn/ExperimentSet")
args = parser.parse_args()

print '==========='

s = requests.Session()
s.headers.update({'Authorization': args.token})
resp_json = s.get(args.url).json()

pretty_json = json.dumps(resp_json, indent=2)
print pretty_json

filename = 'p13_%s.json' % time.strftime('%Y%m%d_%H%M_%S')
text_file = open(filename, "w")
text_file.write(pretty_json)
text_file.close()

print '==========='
print 'output saved to %s' % filename