# -*- coding: utf-8 -*-
# test.py for Rabbit-Python

import unittest
from rabbit import Rabbit

class RabbitTests(unittest.TestCase):
    def setUp(self):
        testing = True

    def test_uni2zg(self):
        print("converting Unicode to Zawgyi")
        converted = Rabbit.uni2zg(u"မင်္ဂလာပါ")
        self.assertEqual(converted, u"မဂၤလာပါ")

        converted = Rabbit.uni2zg(u"ပြင်သစ်ဘာသာကီးဘုတ်")
        self.assertEqual(converted, u"ျပင္သစ္ဘာသာကီးဘုတ္")

    def test_zg2uni(self):
        print("converting Zawgyi to Unicode")
        converted = Rabbit.zg2uni(u"မဂၤလာပါ")
        self.assertEqual(converted, u"မင်္ဂလာပါ")

        converted = Rabbit.zg2uni(u"ျပင္သစ္ဘာသာကီးဘုတ္")
        self.assertEqual(converted, u"ပြင်သစ်ဘာသာကီးဘုတ်")

if __name__ == "__main__":
    unittest.main()
