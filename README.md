# DDNS
DDNS script based on cloudxns and taobaoip
You need to set 

api_url = "https://www.cloudxns.net/api2/record/RECORD_ID"
api_key = "API_KEY"
api_secret = "API_SECRET"
Domain_ID = DOMAIN_ID
ttl = 120
line_id = 1
host = "HOST"
Domain_type = "A"

Here is an example:
api_url = "https://www.cloudxns.net/api2/record/2387630"
api_key = "a7fe5ecbb823e7b0c968b2a885a111e98"
api_secret = "8544d2316d504044"
Domain_ID = 11864
ttl = 120
line_id = 1
host = "home"
Domain_type = "A"

Then you can use cron to run it on time.
