# Brief

Goal of the exercise is to implement a tree/visitor structure that
fulfills the requirement specification provided in the unittest file
`tree_test.py`.

Create the initial class architecture and test it against the structure
tests (remember that you can can create more classes than the strict
necessary, if you think it benefits the *maintanability*). 

Once you've done that, toggle on the functional tests by changing line 8
in `tree_test.py` to:

```python
functionality_tests_off = False
```

Tackle the tests one by one: extend the code to pass one test, refactor
your implementation for readability and expressiveness and then go on
to the next test.


## Running the tests

To run the tests, run the unittest module: python3 -m unittest tree_test.py  

Common pytest options  

 * -v : enable verbose output

For other options, see python -m unittest -h

## Evaluation Criteria

 * Python best practices
 * Completeness: did you complete the features? Are all the tests running?
 * Correctness: does the functionality act in sensible, thought-out ways?
 * Maintainability: is it written in a clean, maintainable way?

## CodeSubmit  

Please organize, design, and document your code as if it were going into
production and send it back to us.   

All the best and happy coding,  

The RiACT Team  
