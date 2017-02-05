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


#<link rel="stylesheet" type="text/css"href="styles.css">

class MainHandler(webapp2.RequestHandler):
    def get(self):

        error = self.request.get("error")
        name_error=self.request.get("name_error")

        submit_form = """
        <form action="/verify" method="post">
            <h1>Signup</h1>
               <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" required>
                        <span style ='color:red'>"""+name_error+"""</span>
                    </td>
                </tr>

                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" required>
                        <span style='color:red'>"""+error+""" </span>
                    </td>
                </tr>

                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify_password" type="password" required>

                    </td>
                </tr>

                <tr>
                   <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                    </td>
                </tr>

            </table>
            <input type="submit">
        </form>
        """
#        header="<h1>Signup</h1>"

#        submit_form="""<form>
#        <form action="/verify" method="post">
#        <br>
#        Username: <input name="username" type="text" value="" required>
#        <br>
#        Password: <input name="password" type="password" required>
#        <br>
#        Verify Password: <input name="verify_password" type="password" required>
#        <br>
#        Email(optional): <input name="email" type="email" value="">
#        <br>
#        <input type="submit">
#        </form>
#        """
        self.response.write(submit_form)

class Validation(webapp2.RequestHandler):

        def post(self):
            username=self.request.get("username")
            check_password=self.request.get("password")
            ver_password=self.request.get("verify_password")

            if " " in username and check_password != ver_password:
                name_error="Invalid username"
                error="Passwords do not match"
                self.redirect("/?name_error=Invalid Username"+"&error=Passwords do not match")

            if " " in username:
                name_error="Invalid username"
                self.redirect("/?name_error=Invalid Username")

            if check_password != ver_password:
               error="Passwords do not match"
               self.redirect("/?error=Passwords do not match")


            self.response.write("<h1>Welcome "+username+"</h1>")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/verify', Validation)

], debug=True)
