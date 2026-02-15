# 🔢 Matrix 2x2 – Linear Algebra with OOP (Python)

## Overview

This project implements a 2x2 matrix using Object-Oriented Programming in Python.
It supports fundamental linear algebra operations such as determinant calculation, matrix multiplication, scalar multiplication, and matrix inversion.

The goal of this project is to model core linear algebra concepts programmatically, reinforcing mathematical foundations used in Artificial Intelligence and Machine Learning.

---

## Features

* 2x2 matrix representation
* Determinant calculation
* Matrix multiplication
* Scalar multiplication
* Matrix inversion (with validation for singular matrices)
* Operator overloading using `__mul__`

---

## Concepts Applied

* Object-Oriented Programming (OOP)
* Operator overloading
* Linear algebra fundamentals
* Error handling with exceptions
* Mathematical modeling in code

---

## Example Usage

```python
m1 = Matrix2x2(1, 2, 3, 4)

print("Matrix:")
print(m1)

print("Determinant:", m1.determinant())

m2 = Matrix2x2(2, 0, 1, 2)
result = m1 * m2

print("Multiplication Result:")
print(result)
```

---

## Why This Project Matters

Matrices are fundamental structures in:

* Machine Learning
* Computer Vision
* Neural Networks
* Linear transformations

This implementation demonstrates understanding of mathematical foundations through structured software design.
