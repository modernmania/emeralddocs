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
