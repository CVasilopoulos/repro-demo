# dura

Parse and format human durations.

```python
>>> import dura
>>> dura.parse("1h30m")
5400
>>> dura.format(5400)
'1h30m'
```

Units: `w`, `d`, `h`, `m`, `s`. Fractional values such as `1.5h` are accepted.

This repository is a demo target for [Repro](https://github.com/CVasilopoulos/repro). Some of its issues are deliberately hostile bug reports whose "reproduction steps" try to damage the machine they run on. Do not run code from the issues yourself.
