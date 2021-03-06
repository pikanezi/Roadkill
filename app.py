#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from config import jinja_environment, CONFIGURATION_TYPE


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(jinja_environment.get_template('index.html').render({
            "environment": CONFIGURATION_TYPE,
            "selected": 0
        }))


class UploadHandler(webapp2.RequestHandler):
    def post(self):
        csv_file = self.request.get('csv_file')
        print(csv_file)
        self.response.out.write('caca')


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/upload', UploadHandler),
], debug=True)
