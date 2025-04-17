# Introduction to Python

## Getting Started with Python

Python is an interpreted, high-level, and general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.

To check if Python is installed on your system, you can run `python --version` in your command line. If Python is not installed, you can download it from [python.org](https://www.python.org/). For detailed installation instructions, you can refer to [W3Schools Python Get Started](https://www.w3schools.com/python/python_getstarted.asp).

To run a Python file, navigate to the directory containing your file and use the command:

```bash
python filename.py
```

## Python Syntax

Python syntax is designed to be readable and straightforward. Key points include:

- **Indentation**: Python uses indentation to define blocks of code. Consistent indentation is crucial. Unlike many other languages, Python does not use curly braces to delimit blocks of code. For example:

  ```python
  if True:
      print("This is indented correctly")
  # Incorrect indentation
  if True:
  print("This will cause an IndentationError")
  ```

  Indentation is not just for readability; it is a part of the syntax. All lines of code in a block must have the same indentation level.

- **Line Structure**: Each line in Python is a statement. Statements do not need to end with a semicolon, although they can be used to separate multiple statements on a single line. For example:

  ```python
  x = 5; y = 10
  print(x + y)
  ```

  While semicolons are optional, they can be useful for writing concise code.

- **Case Sensitivity**: Python is case-sensitive, which means `Variable` and `variable` would be considered two different identifiers. For example:

  ```python
  name = "Alice"
  Name = "Bob"
  print(name)  # Outputs: Alice
  print(Name)  # Outputs: Bob
  ```

  This is important to remember when defining and using variables.

## Python Comments

Comments are used to explain code and are not executed by the interpreter. Python supports:

- **Single-line comments**: Start with a `#` symbol. They can be placed at the beginning of a line or after a statement. For example:

  ```python
  # This is a single-line comment
  x = 5  # This is an inline comment
  ```

  Comments are essential for code documentation and can help others understand your code.

- **Multi-line comments**: Use triple quotes (`'''` or `"""`). These are often used for documentation strings (docstrings) in functions and classes. For example:

  ```python
  """
  This is a multi-line comment
  or docstring.
  """
  def example_function():
      pass
  ```

  Docstrings are a standard way to document Python functions, modules, and classes.

## Python Variables

Variables in Python are used to store data. You do not need to declare a variable type explicitly. For example:

```python
x = 5
name = "Alice"
```

Variables can store different data types, and their type can change dynamically. Python supports various data types, including integers, floats, strings, lists, tuples, sets, and dictionaries. Variables are created when you assign a value to them, and they can be reassigned to different data types as needed.

### Naming Conventions

- Variable names must start with a letter or an underscore (_), followed by letters, numbers, or underscores.
- Variable names are case-sensitive.
- Avoid using Python reserved words as variable names.

Examples of valid variable names:

```python
my_variable = 10
_variable = "underscore"
variable123 = 5.5
```

Examples of invalid variable names:

```python
1variable = 10  # Cannot start with a number
my-variable = 5  # Hyphens are not allowed
class = "reserved"  # 'class' is a reserved word
```

## Operations

Python supports various operations, including arithmetic, comparison, and logical operations. Here are some examples:

- **Arithmetic Operations**: Addition, subtraction, multiplication, division, etc.

  ```python
  a = 10
  b = 5
  print(a + b)  # Outputs: 15
  print(a - b)  # Outputs: 5
  print(a * b)  # Outputs: 50
  print(a / b)  # Outputs: 2.0
  ```

  Python also supports exponentiation and modulus operations:

  ```python
  print(a ** b)  # Outputs: 100000, which is 10 to the power of 5
  print(a % b)  # Outputs: 0, the remainder of 10 divided by 5
  ```

- **Operator Precedence**: Python follows the standard mathematical precedence rules.

  ```python
  result = 10 + 5 * 2  # Outputs: 20, because multiplication has higher precedence than addition
  ```

- **Comparison and Logical Operations**: Used to compare values and combine logical statements.

  ```python
  print(a > b)  # Outputs: True
  print(a == b)  # Outputs: False
  print(a != b and a > b)  # Outputs: True
  ```

  Logical operators include `and`, `or`, and `not`, which can be used to build complex logical expressions.
