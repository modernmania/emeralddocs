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
