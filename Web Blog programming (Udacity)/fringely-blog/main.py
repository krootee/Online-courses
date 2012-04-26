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
from string import maketrans
import webapp2
import cgi
import codecs
import re

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
month_dict = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_dict.get(short_month)

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day < 32:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2012:
            return year

def escape_html(s):
    return cgi.escape(s, quote=True)

form="""
<form method="post" action="/birthday">
    What is your birthday?
    <br>
    <label> Month
        <input text="text" name="month" value="%(month)s">
    </label>
    <label> Day
        <input text="text" name="day" value="%(day)s">
    </label>
    <label> Year
        <input text="text" name="year" value="%(year)s">
    </label>
    <div style="color:red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {'error': escape_html(error),
                                        'month': escape_html(month),
                                        'day': escape_html(day),
                                        'year': escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        year = valid_year(user_year)
        day = valid_day(user_day)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

# ROT13
# add 13 to chars
# do escaping of txt

rot13form="""
<form method="post" action="/rot13">
    Enter text to be rot13-ed:
    <br>
    <textarea name="text">%(value)s</textarea>
    <br>
    <input type="submit">
</form>
"""

class Rot13Handler(webapp2.RequestHandler):
    def write_form(self, value=""):
        self.response.out.write(rot13form % {'value' : value})

    def get(self):
        self.write_form()

    def post(self):
        value = self.request.get('text')
        result = value.encode('rot13')
        self.write_form(escape_html(result))

user_signup_form="""
<form method="post" action="/user_signup">
    <bold>Signup</bold>
    <br>
    <label>
        Username
        <input type="text" name="username" value="%(username)s">
    </label>
    <br>
    <label>
        Password
        <input type="password" name="password">
    </label>
    <br>
    <label>
        Verify Password
        <input type="password" name="verify">
    </label>
    <br>
    <label>
        Email (optional)
        <input type="text" name="email" value="%(email)s">
    </label>
    <br>
    <input type="submit">
</form>
"""

class UserSignupFormHandler(webapp2.RequestHandler):
    def write_form(self, username="", email=""):
        self.response.out.write(user_signup_form % {'username' : username, 'email' : email})

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        username_check = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        password_check = re.compile(r"^.{3,20}$")
        email_check = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

        valid_username = username_check.match(username)
        valid_password = password_check.match(password)

        if (len(email) > 0):
            valid_email = email_check.match(email)
        else:
            valid_email = True

        if (password == verify):
            passwords_match = True
        else:
            passwords_match = False

        if (valid_username and valid_password and passwords_match and valid_email):
            self.redirect("/signup_thanks?username=%s" % username)
        else:
            self.write_form(escape_html(username), escape_html(email))

class SignupThanksHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.out.write("Welcome, %s!" % username)

app = webapp2.WSGIApplication([('/birthday', MainHandler),
                               ('/rot13', Rot13Handler),
                               ('/thanks', ThanksHandler),
                               ('/user_signup', UserSignupFormHandler),
                               ('/signup_thanks', SignupThanksHandler)], debug=True)
