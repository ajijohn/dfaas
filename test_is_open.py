from dfaas import DFAASApiClient

import sys
import unittest

global KEY
global IP


class IsOKTest(unittest.TestCase):

    def test_ok_check(self):
        dfaas_client = DFAASApiClient(KEY,IP)
        self.assertEqual(dfaas_client.hello(),"ok")



if __name__ == '__main__':
    print("Please enter DFAAS api key")
    KEY = sys.stdin.readline().strip()
    print(KEY)
    print("Please enter DFAAS cluster IP")
    IP = sys.stdin.readline().strip()
    print(IP)
    unittest.main()
