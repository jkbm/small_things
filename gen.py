import json
import logging

config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG},
        'file': {
                'class': 'logging.FileHandler',
                'filename': 'mplog.log',
                'mode': 'w',
                'formatter': 'f',
            }
        },
    root = {
        'handlers': ['h', 'file'],
        'level': logging.DEBUG,
        },
    
)
	
with open('log-config.json', 'w') as f:
	f.write(json.dumps(config))