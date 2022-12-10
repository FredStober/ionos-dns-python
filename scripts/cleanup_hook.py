#!/usr/bin/env python
""" Module to create authentication DNS records for letsencrypt """
import json
import logging
import os
import sys
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

    log.info('Getting DNS zone...')
    domain_name = os.environ['CERTBOT_DOMAIN']
    zone_id = dns.get_zone_id(domain_name)
    log.info('DNS zone ID: %s', zone_id)

    log.info('Getting DNS zone records...')
    validation_str = os.environ['CERTBOT_VALIDATION']
    zone_info = dns.get_zone(zone_id)
    for record_info in zone_info['records']:
        log.info('Processing DNS zone record: %s', record_info)
        if record_info['name'].startswith('_acme-challenge.'):
            if record_info['content'] == f'"{validation_str}"':
                record_id = record_info['id']
                log.info('Deleting DNS record: %s', record_id)
                dns.delete_record(zone_id, record_id)
                log.info('DNS record deleted')


if __name__ == '__main__':
    main()
