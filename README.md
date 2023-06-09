# debug-viz-demo
> Debug Visualization Demo for Ada

# Why
* It looks amazing!
* An intresting architecture
* Ideas for GNAT Studio

## You need
* VSCode
* [Debug Visualization](https://marketplace.visualstudio.com/items?itemName=hediet.debug-visualizer) extension
* [Native Debug](https://marketplace.visualstudio.com/items?itemName=webfreak.debug) extension

## Sequence diagram:

```plantuml
@startuml
actor       User       as User
User       -> Visualizer: Expression
Visualizer -> DAP: DAP Request
DAP        -> GDB: GDB-MI command
GDB        -> DAP: JSON as String
DAP        -> Visualizer: DAP Response
Visualizer -> User: WebView Content
@enduml
```
![Round-trip diagram](image/round-trip.png)


While the extension is a language agnostic
JSON is parsed from C/C++/JS string literal, but Ada literal has a distinct syntax for escape quotes and non-ASCII characters. So we need hacks right now.

To overcome, let's change language:

    --language minimal $vizText(Text)

Glue code could be
* in Python (using GDB Python API)
* in Ada (with External_Name to work with minimal lang)

### Python

This glue code defines three functions (`$vizText`, `$vizGrid`, `$vizPlot`).

    source src/aaa.py
    set print elements unlimited

    --language minimal $vizPlot(List)

### Ada

This Python script defines `$vizCall` function to call glue code
in defined in Ada. It accepts function name and its argument.
This will find a global function with given name
and call it with given argument. The Ada function
should return String. The result will be converted
to plain Python string with escape characters stripped.
Ada function should have `External_Name` to be called from
`minimal` language:

    source src/bbb.py
    set print elements unlimited

    --language minimal $vizCall("something", 1)
