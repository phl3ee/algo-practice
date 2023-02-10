# Algo Practice

Just revisting python with algo practice from leetcode etc

Some of these are not unit tested, I just copied my solutions off the platform to have them locally, after setting up a local dev environment.

## Usage

Run tests from root directory like this:

```python
 python -m unittest tests.test_twoSum
```

Put up a new test and algo package stub like this:

```cmd
python ./putup_algo.py -h
python ./putup_algo.py -p 'a_package' -f 'def removeDuplicates(self, nums: List[int]) -> int:' -d 'Just a test'
```

### TO-DOs

- Parse leetcode URL to generate input for the putup/scaffolding
- resolve non-PEPyness