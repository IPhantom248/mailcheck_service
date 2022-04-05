from __future__ import absolute_import

import traceback

import httpx
import redis

from main.celery import BROKER_URL, app


@app.task(name="run_refresh_domains")
def refresh_domains():
    r = redis.from_url(BROKER_URL)
    disposable_domains_count = r.scard("disposable_domains")

    urls = [
        "https://www.stopforumspam.com/downloads/toxic_domains_whole.txt",
        "https://raw.githubusercontent.com/disposable/disposable-email-domains/master/domains.txt",
    ]
    for url in urls:
        try:
            response = httpx.get(url)
            domains = [domain.rstrip("\n") for domain in response.iter_lines()]
            r.sadd("disposable_domains", *domains)
        except:
            print(traceback.format_exc())

    url = "https://web2.temp-mail.org/mailbox"
    try:
        for _ in range(0, 10):
            response = httpx.post(url)
            data = response.json()
            mailbox = data["mailbox"]
            domain = mailbox.split("@")[1]
            r.sadd("disposable_domains", domain)
    except:
        print(traceback.format_exc())

    url = "https://api.internal.temp-mail.io/api/v4/domains"
    try:
        response = httpx.get(url)
        data = response.json()
        domains = data["domains"]
        for domain in domains:
            r.sadd("disposable_domains", domain["name"])
    except:
        print(traceback.format_exc())

    cur_disposable_domains_count = r.scard("disposable_domains")
    updated = cur_disposable_domains_count - disposable_domains_count
    print(f"Disposable domains: {cur_disposable_domains_count} Updated: {updated}")
