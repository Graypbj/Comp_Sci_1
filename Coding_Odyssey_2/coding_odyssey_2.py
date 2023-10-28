# This will be my coding odyssey. I would like to make an online scrubber that looks for maybe Bill Hader on the
# front page of YouTube.
# I could have it run for multiple days, collect the data, and see how popular he is at different points in time.

import urllib.request
from urllib.request import urlopen

url = "https://www.youtube.com/"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
