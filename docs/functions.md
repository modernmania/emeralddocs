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
