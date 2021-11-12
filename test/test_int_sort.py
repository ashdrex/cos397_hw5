# =========================================================================
#
#  Copyright COS 397
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================
import numpy as np

"""
These functions test the sorting algorithms in the /sort_lib/int_sort.py file.

Notes to Self:
    Not sure what self is suppose to do here...
"""

class TestIntSort:
    def is_sorted(self, int_list):
        sorted_list = int_list
        for i in range(len(sort_list)-1):
            if sorted_list[i]<sorted_list[i-1]:
                assert False
        assert True
    def test_bubble(self, int_list):
        sorted_list = bubble(int_list)
        for i in range(len(sort_list)-1):
            if sorted_list[i]<sorted_list[i-1]:
                assert False
        assert True
    def test_quick(self, int_list):
        sorted_list = quick(int_list)
        for i in range(len(sort_list)-1):
            if sorted_list[i]<sorted_list[i-1]:
                assert False
        assert True
    def test_insertion(self, int_list):
        sorted_list = insertion(int_list)
        for i in range(len(sort_list)-1):
            if sorted_list[i]<sorted_list[i-1]:
                assert False
        assert True				  
        
intlist = np.random.randint(1,100,100)
