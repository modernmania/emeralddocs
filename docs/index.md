# Emerald Documentation
  **Welcome** to the documentation for the Emerald programming language!
  [GitHub](https://github.com/GemCreative/Emerald)

## 1. Installation

Install both binaries from the official releases page:

- Emerald Compiler
- Emerald Shell

Download them from:

- `https://github.com/GemCreative/Emerald/releases`

## 2. Getting Started

### File Types

- Source file: `.emer`
- Compiled bytecode file: `.emec`

### CLI

From `src/`:

```powershell
go run main.go build ..\examples\hello.emer
go run main.go run ..\examples\hello.emer
go run main.go run ..\examples\hello.emec
```

You can also build `main.go` into a binary and run the same commands:

```powershell
emerald build file.emer
emerald run file.emer
emerald run file.emec
```

## 3. Syntax Basics

- Line-oriented statements.
- Blocks use braces `{ ... }`.
- Comments start with `#` or `--`.
- Strings use single quotes `'text'` or double quotes `"text"`.
- Identifiers: letters/underscore first, then letters/digits/underscore.

Example:

```emer
# this is a comment
var name = "Emerald"
print(name)
```

## 4. Types

Emerald runtime values:

- `int`
- `string`
- `bool`
- `null`
- `list`
- `dict`

Type annotations are optional but supported in `var` declarations and function params/returns.

Supported type names:

- `int`
- `str` or `string`
- `bool`
- `null`
- `list`
- `dict` or `table`

## 5. Variables

### Single Declaration

```emer
var a = 10
var b(int) = 20
var name(str) = "Ada"
var empty
```

### Block Declaration

```emer
var {
  name(str)=("Ada"),
  age(int)=(20),
  active(bool)=(true)
}
```

### Assignment

```emer
var x = 1
x = x + 10
```

Index assignment is supported:

```emer
var xs = [1, 2, 3]
xs[1] = 99

var d = dict("a", 1)
d["b"] = 2
```

## 6. Expressions

### Literals

```emer
123
"hello"
'hello'
true
false
null
[1, 2, 3]
```

### Operators

- Unary: `not`, `-`
- Binary: `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `and`, `or`

Notes:

- `+` supports int addition, string concatenation, list concatenation.
- `/` is integer division.

### Indexing

```emer
var xs = [10, 20, 30]
print(xs[0])     # 10
print(xs[-1])    # 30

var d = dict("name", "emerald")
print(d["name"]) # emerald

var s = "hello"
print(s[1])      # e
```

### Slicing

Works on lists and strings:

```emer
var xs = [1, 2, 3, 4]
print(xs[1:3])   # [2, 3]
print(xs[:2])    # [1, 2]
print(xs[2:])    # [3, 4]

var s = "hello"
print(s[1:4])    # ell
```

## 7. String Interpolation (f-strings)

Use `f"..."` with `{expr}`:

```emer
var name = "Ada"
var n = 5
print(f"Hello {name}, n={n}, sum={n+1}")
```

Interpolation compiles to string concatenation behavior.

## 8. Statements

### print

```emer
print("Hello")
print(1 + 2)
```

### input

Modern forms:

```emer
var a = input()
var b = input("Name: ")
var c = read("Prompt: ")  # alias
```

Legacy form is still accepted:

```emer
input(plc("Name: "))
```

### wait

```emer
wait(500)  # milliseconds
```

### check

Fails at runtime if expression is falsy:

```emer
check 1 == 1
check len([1]) > 0
```

### return

```emer
return
return 42
```

## 9. Control Flow

### if / else if / else

```emer
if(x > 10) {
  print("big")
} else if(x == 10) {
  print("equal")
} else {
  print("small")
}
```

### while

```emer
while(x < 5) {
  x = x + 1
}
```

### for(condition)

```emer
for(true) {
  print("loop")
  brk
}
```

### for-in

```emer
var xs = [10, 20, 30]
for(item in xs) {
  print(item)
}
```

### Loop control

```emer
brk   # break
cont  # continue
```

## 10. Functions

### Declaration

```emer
fnc greet {
  print("hello")
}
```

### With params

```emer
fnc add(a, b) {
  return a + b
}
```

### Typed params and return

```emer
fnc add(a(int), b(int)) (int) {
  return a + b
}
```

### Call

```emer
print(add(2, 3))
```

## 11. Built-in Functions

### Data Structure Builtins

- `dict(k1, v1, k2, v2, ...)`
- `table(...)` (alias of `dict`)
- `len(obj)` where `obj` is string/list/dict
- `append(list, item)` returns a new list
- `keys(dict)` returns list of string keys

Example:

```emer
var d = dict("a", 1, "b", 2)
print(len(d))
print(keys(d))

var xs = [1, 2]
xs = append(xs, 3)
print(xs)
```

### Input Builtins

- `input()`
- `input(prompt)`
- `read()` / `read(prompt)` (alias)
- `plc(x)` returns string form of `x` (mainly for legacy `input(plc(...))`)

### Math Builtins

- `math_abs(x)`
- `math_min(a, b)`
- `math_max(a, b)`
- `math_pow(a, b)`

Example:

```emer
print(math_abs(-7))
print(math_min(10, 4))
print(math_max(10, 4))
print(math_pow(2, 5))
```

## 12. Truthiness

Falsy values:

- `null`
- `false`
- `0`
- `""`
- `[]`
- `{}`

Everything else is truthy.

## 13. Scoping Rules

- Top-level variables are global.
- Functions use local slots (fast local access).
- Block scopes inside functions allow shadowing.

Example:

```emer
fnc demo() {
  var x = 10
  if(true) {
    var x = 20
    print(x) # 20
  }
  print(x)   # 10
}
```

## 14. Errors and Traceback

Runtime failures include traceback with function and line numbers.

Example output:

```text
Runtime error: division by zero
Traceback:
  at b (line 5)
  at a (line 2)
  at <main> (line 7)
```

## 15. Current Limitations

- No floating-point type (only int).
- No `<=` / `>=`.
- No object/module import system yet.
- No classes/struct runtime model yet.
- Dict iteration via `for-in` is not specialized yet; prefer `for(k in keys(dictVal))`.

## 16. Practical Example

```emer
var nums = [1, 2, 3, 4]
var squares = []

for(n in nums) {
  squares = append(squares, math_pow(n, 2))
}

print(f"squares = {squares}")

fnc findFirstBig(xs(list), threshold(int)) (int) {
  for(v in xs) {
    if(v > threshold) {
      return v
    }
  }
  return -1
}

print(findFirstBig(squares, 10))
```
