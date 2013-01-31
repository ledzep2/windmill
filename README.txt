New Proxy Chain feature:

Configure proxy chain in your prefs.py file like this

HTTP_PROXY = "proxy_host:port"

or

HTTP_PROXY_RULES = {
    "proxy_host:port": [
        "*.a.com",
        "*.b.com",
        ...
    ],
    ...
}

for proxy rules, if none of the rules matches, HTTP_PROXY or none will be used.


==============================

Windmill is currently a very active work-in-progress so the best place
to find up-to-date information would be online:

  http://wiki.github.com/windmill/windmill/

Another great location is the mailing list:

  http://groups.google.com/group/windmill-dev
