from __future__ import absolute_import, unicode_literals
from celery import shared_task
import nmap

@shared_task
def get_devices():
    nm = nmap.PortScanner()
    nm.scan('192.168.0.1/24', '-A')
    return nm.all_hosts()