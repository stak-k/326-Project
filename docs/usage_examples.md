# Usage Examples

This document demonstrates how to use and how to use and test the functions in the ** Rental Hunters Function Library **.

Each example below shows expected outputs and common error cases.

## Simple Functions

###  `validate_rental_address(address)`
```python
validate_rental_address("123 Main St, Springfield, IL 62704")
validate_rental_address("")
Output: True
Error Example: Address cannot be empty
