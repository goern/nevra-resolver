#!/usr/bin/env python3
#

import logging
import json
import http

import tornado.httpserver
import tornado.ioloop
import tornado.web

from tornado import gen
from tornado.escape import json_decode, json_encode

import dnf.subject
import hawkey

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        q = None

        try:
            q = self.get_query_argument('q')
        except tornado.web.MissingArgumentError as mae:
            logging.error(mae)
            self.set_status(http.HTTPStatus.BAD_REQUEST)
            self.write("No query argument 'q' provided")

        if q:
            logging.debug("nevra'ing q=%s" % q)

            subject = dnf.subject.Subject(q)

            results = []

            for nevra_obj in subject.get_nevra_possibilities(forms=[hawkey.FORM_NEVRA]):
                # nevra_obj.name, nevra_obj.epoch, nevra_obj.version, nevra_obj.release, nevra_obj.arch

                result = {}
                result['name'] = nevra_obj.name
                result['version'] = nevra_obj.version
                result['release'] = nevra_obj.release
                result['arch'] = nevra_obj.arch

                results.append(result)

            self.write(json.dumps(results))


def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
