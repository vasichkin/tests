# Copyright (c) 2013 Qubell Inc., http://qubell.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "Vasyl Khomenko"
__email__ = "vkhomenko@qubell.com"
__copyright__ = "Copyright 2014, Qubell.com"
__license__ = "Apache"

from unittest.case import skip

from unittest import TestCase

class TestSelenium(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSelenium, cls).setUpClass()
        print "Run before all methods"

    @classmethod
    def tearDownClass(cls):
        super(TestSelenium, cls).tearDownClass()
        print "Run after all methods"


    def setUp(self):
        print "Run before every test"

    def tearDown(self):
        print "Run after every test"

    def test_one(self):
        assert True

    @skip('Test broken')
    def test_fail(self):
        assert False

    def test_tttt(self):
        pass
    def test_tttt1(self):
        pass
    def test_tttt2(self):
        pass
    def test_tttt3(self):
        pass


    def test_tttt5(self):
        pass