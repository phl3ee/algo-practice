"""Helper for building out test and code stubs for new algo.

Parameters:
    - Package name
    - Function definition from leetcode
    - Description (optional)

Example:
python ./putup_algo.py -p 'a_package' -f 'def removeDuplicates(self, nums: List[int]) -> int:' -d 'Just a test'

"""
import argparse

#We can consume the leetcode URL and populate the params (and examples)
#   https://leetcode.com/problems/remove-duplicates-from-sorted-array/
parser = argparse.ArgumentParser(description='Build leetcode package and test stubs')
parser.add_argument("-p", "--package_name", type=str, help='The name of your package file.')
parser.add_argument("-f", "--function_definition", type=str,
                    help='The function definition from leetcode'
                    )
parser.add_argument("-d", "--description", type=str, help='The description/intro from leet code')

args          = parser.parse_args()
package_name  = args.package_name.strip()
function_definition  = args.function_definition.strip()
description   = args.description
algo_name     = function_definition.split(' ')[1].replace('(self,','')

test_template = './scaffold/test_template.txt'
test_output   = "./tests/test_" + package_name + ".py"
algo_template = './scaffold/algo_template.txt'
algo_output   = "./algos/" + package_name + ".py"
algo_init     = "./algos/__init__.py"

#clone, update, insert test case
with open(test_template, 'r') as file:
    test_data = file.read()
    #Crudely chopping up description field to reduce line length
    test_data = test_data.replace('<DESCRIPTION>', description.replace(',',',\n').replace('.','.\n'))
    test_data = test_data.replace('<PACKAGE_NAME>', package_name)
    test_data = test_data.replace('<ALGO>', algo_name)

with open(test_output, 'w') as file:
    file.write(test_data)

#clone, update, insert algo
with open(algo_template, 'r') as file:
    algo_data = file.read()
    algo_data = algo_data.replace('<FUNCTION>', function_definition)

#add local imports if the function has lists, ListNodes etc
if 'ListNode' in function_definition:
    algo_data = 'from helpers.listNodeHelpers import ListNode\n' + algo_data
if 'TreeNode' in function_definition:
    algo_data = 'from helpers.tree_node import TreeNode\n' + algo_data
if 'List[' in function_definition:
    algo_data = 'from typing import List\n' + algo_data
if 'Optional' in function_definition:
    algo_data = 'from typing import Optional\n' + algo_data

with open(algo_output, 'w') as file:
    file.write(algo_data)

#add algo and package to __init__
with open(algo_init, 'r') as file:
    data = file.read()
    data = data + "\nfrom ." + package_name + " import Solution"
with open(algo_init, 'w') as file:
    file.write(data)


print("******************************************")
print("All done, new tests and package generated")
print("******************************************")
print("Run tests with:")
print("python -m unittest tests.test_" + package_name + " -v")
print("\nAlgo source is here:")
print(algo_output)
print("\nglhfdd...")
print("******************************************")
