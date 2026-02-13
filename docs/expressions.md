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
