# Emerald


## 1. Overview

Emerald is a programming language with:

- `.emer` source files
- `.emec` compiled bytecode files (JSON in the current C# implementation)
- Integer math, strings, booleans, lists, dictionaries
- Functions, control flow, and a stack-based VM runtime

## 2. Command Line

### Core Commands

- `emerald build <file.emer>`
- `emerald run <file.emer|file.emec>`
- `emerald shell`

### Direct Utility Commands

- `emerald touch <file>.emer`
- `emerald carve <file>.emer`
- `emerald shine <file>.emer`

`shine` compiles then runs the target file.

## 4. File Types

- Source: `.emer`
- Compiled: `.emec`

Note: Current `.emec` format is JSON from the C# implementation. It is not compatible with older Go `gob` `.emec` files.

## 5. Syntax Basics

- Statements are line-oriented.
- Blocks use `{ ... }`.
- Comments begin with `#` or `--`.
- Strings use `'text'` or `"text"`.
- Identifiers: letter/underscore first, then letters/digits/underscore.

Example:

```emer
# comment
var name = "Emerald"
print(name)
```

## 6. Types

Runtime value kinds:

- `int`
- `string`
- `bool`
- `null`
- `list`
- `dict`

Supported type names in declarations:

- `int`
- `str` / `string`
- `bool`
- `null`
- `list`
- `dict` / `table`

## 7. Variables

### Single declarations

```emer
var a = 10
var b(int) = 20
var name(str) = "Ada"
var empty
```

### Block declarations

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

Index assignment:

```emer
var xs = [1, 2, 3]
xs[1] = 99

var d = dict("a", 1)
d["b"] = 2
```

## 8. Expressions

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

- `+` supports int addition, string concat, list concat.
- `/` is integer division.

### Indexing

```emer
var xs = [10, 20, 30]
print(xs[0])
print(xs[-1])

var d = dict("name", "emerald")
print(d["name"])

var s = "hello"
print(s[1])
```

### Slicing

```emer
var xs = [1, 2, 3, 4]
print(xs[1:3])
print(xs[:2])
print(xs[2:])

var s = "hello"
print(s[1:4])
```

## 9. String Interpolation

Use f-strings:

```emer
var name = "Ada"
var n = 5
print(f"Hello {name}, n={n}, sum={n+1}")
```

## 10. Statements

### print

```emer
print("Hello")
print(1 + 2)
```

### input / read

```emer
var a = input()
var b = input("Name: ")
var c = read("Prompt: ")
```

Legacy form supported:

```emer
input(plc("Name: "))
```

### wait

```emer
wait(500)
```

### check

```emer
check 1 == 1
check len([1]) > 0
```

### return

```emer
return
return 42
```

## 11. Control Flow

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

- `brk`
- `cont`

## 12. Functions

### Simple

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

### Typed params + return

```emer
fnc add(a(int), b(int)) (int) {
  return a + b
}
```

### Call

```emer
print(add(2, 3))
```

## 13. Built-ins

### Data

- `dict(k1, v1, k2, v2, ...)`
- `table(...)` (alias)
- `len(obj)`
- `append(list, item)`
- `keys(dict)`

### I/O

- `input()`
- `input(prompt)`
- `read()` / `read(prompt)`
- `plc(x)`

### Math

- `math_abs(x)`
- `math_min(a, b)`
- `math_max(a, b)`
- `math_pow(a, b)`

## 14. Truthiness

Falsy values:

- `null`
- `false`
- `0`
- `""`
- empty list `[]`
- empty dict `{}`

Everything else is truthy.

## 15. Scoping

- Top-level variables are global.
- Functions use local slots.
- Nested blocks in functions can shadow names.

## 16. Errors and Traceback

Runtime failures include traceback frames with function + line:

```text
Runtime error: division by zero
Traceback:
  at b (line 5)
  at a (line 2)
  at <main> (line 7)
```

## 17. Shell Command Details

Inside `emerald shell`:

- `touch file.emer` creates file if missing
- `carve file.emer` opens editor (`$EDITOR`, else `notepad` on Windows, `vi` on non-Windows)
- `shine file.emer` builds and runs
- `quit` / `exit` leaves shell

## 18. Limitations

Current language/runtime limits:

- No float type (int only)
- No `<=` or `>=`
- No module/import system
- No classes/structs
- Dict iteration is not specialized; use `keys(dict)` in `for-in`

## 19. Example Program

```emer
var nums = [1, 2, 3, 4]
var squares = []

for(n in nums) {
  squares = append(squares, math_pow(n, 2))
}

print(f"squares = {squares}")
```

# 20

: Where to mine from here

There is so much more to do with Emerald! Share projects, make them, and have fun.

### Social Links :

**Github** : https://github.com/GemCreative/Emerald

**Reddit** : https://www.reddit.com/r/emerald_lang/

**Discord** (Not for just Emerald, but all scripting in general!) https://discord.gg/YSjFANtCd4

## Keep on mining!
