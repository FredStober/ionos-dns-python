#!/usr/bin/env python
""" Module to create authentication DNS records for letsencrypt """
import json
import logging
import os
import sys
import time
from pathlib import Path

sys.path.append(Path(__file__).absolute().parent.parent.as_posix())

import ionos.dns


def main() -> None:
    """ Main method to perform letsencrypt authentication """
    log_file = os.path.abspath(__file__).rsplit('.', 1)[0] + '.log'
    logging.basicConfig(format='%(asctime)-15s %(message)s',
                        filename=log_file,
                        level=logging.DEBUG)
    log = logging.getLogger()

    log.info('Reading secrets...')
    with open(os.path.join(os.path.dirname(__file__), 'key.json'),
              encoding='utf-8') as file_obj:
        key_info = json.load(file_obj)

    log.info('Creating DNS interface...')
    dns = ionos.dns.DNS(key_info['prefix'] + '.' + key_info['secret'])

    log.info('Preparing DNS record...')
    domain_name = os.environ['CERTBOT_DOMAIN']
    validation_str = os.environ['CERTBOT_VALIDATION']
    dns_record = {
        'name': f'_acme-challenge.{domain_name}',
        'type': 'TXT',
        'content': validation_str,
        'ttl': 3600,
        'prio': 10,
        'disabled': False,
    }
    log.info('Validation record: %s', dns_record)

    log.info('Getting DNS zone...')
    zone_id = dns.get_zone_id(domain_name)
    log.info('DNS zone ID: %s', zone_id)

    log.info('Creating DNS record...')
    dns.create_records(zone_id, [dns_record])

    time.sleep(10)


if __name__ == '__main__':
    main()
