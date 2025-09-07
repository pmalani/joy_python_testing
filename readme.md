# Joy of Unit-Testing in Python

## Setup—Pretend File System
- Write a class `File`
  - Add `size` property / attribute / field
- Write a class `Folder` and implement
  - We can add `File`(s) to `Folder`
  - We can add other `Folder`(s) to a `Folder`

## Value-based unit-testing
- Implement `size` in folder that sums up all the sizes of files and folder within
- To do Test Driven Development (TDD) or not?
- What test-cases?

## Interaction-based unit-test
- Implement `Shortcut` class
  - We can have a `Shortcut` to a `File`, `Folder`, or another `Shortcut`
  - We can add `Shortcut` to a `Folder`
  - Write a method `open` on `Shortcut`
    - Calls `open` on the underlying `File`, `Folder`, or `Shortcut`
- To do Test Driven Development (TDD) or not?
- What test-cases?

## Recommendations

### Recommendation: Unit-test class per method under test
- Not, unit-test-class per class under test
- What is a unit?
  - method / function
  - not a class
- [test_pfs_folder_size.py](test_pfs_folder_size.py)

### Recommendation: Use data-driven techniques
- [test_pfs_folder_size_ddt.py](test_pfs_folder_size_ddt.py)
- reduces boiler-plate code
- easier to expose edge cases
  - `-1` as file size?

### Recommendation: Use mock for interaction-based unit-testing
- mocking a method
  - [test_pfs_shortcut_open.py](test_pfs_shortcut_open.py)
  - verify the interaction (e.g. `assert_called_once`)
- mocking a class
  - [test_pfs_folder_size_mock.py](test_pfs_folder_size_mock.py)
  - we combined the value-based and interaction-based techniques!
- whereas value-based testing may feel "natural"
  - interaction-based testing may feel "unnatural"

### Recommendation: Clearly organize with a uni-test
- use popular: given, when, then
  - or, other such as arrange, act, assert (AAA)
- [test_pfs_shortcut_open.py](test_pfs_shortcut_open.py)

## Summary
- Write unit-tests
  - Where a unit is a function / method
- Use TDD
- Leverage the popular given, when, then to structure tests
- Use data-driven to reduce duplicate code
- Employ mocks to perform interaction-based unit-testing between collaborators 

## Bonus / Homework
- What design pattern best captures the relation between:
  - `File` and `Folder`
  - `File` and `Shortcut`
