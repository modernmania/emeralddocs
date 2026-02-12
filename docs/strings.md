## 7. String Interpolation (f-strings)

Use `f"..."` with `{expr}`:

```emer
var name = "Ada"
var n = 5
print(f"Hello {name}, n={n}, sum={n+1}")
```

Interpolation compiles to string concatenation behavior.
