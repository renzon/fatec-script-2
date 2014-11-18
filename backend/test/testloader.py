#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import webapp2
from webapp2_extras import i18n
import os
import settings

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
ROOT_PATH = os.path.dirname(__file__)


#workaroung for i18n

app = webapp2.WSGIApplication(
    [webapp2.Route('/', None, name='upload_handler')])

request = webapp2.Request({'SERVER_NAME': 'test', 'SERVER_PORT': 80,
                           'wsgi.url_scheme': 'http'})
request.app = app
app.set_globals(app=app, request=request)

i18n.default_config['default_locale'] = 'en_US'
i18n.default_config['default_timezone'] = settings.DEFAULT_TIMEZONE
if __name__ == '__main__':
    if 'GAE_SDK' in os.environ:

        SDK_PATH = os.environ['GAE_SDK']

        sys.path.insert(0, SDK_PATH)

        import dev_appserver
        dev_appserver.fix_sys_path()

    sys.path.append(os.path.join(PROJECT_PATH, 'src'))

    tests = unittest.TestLoader().discover(ROOT_PATH, "*.py")
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)
