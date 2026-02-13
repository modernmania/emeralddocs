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
