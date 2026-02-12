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
