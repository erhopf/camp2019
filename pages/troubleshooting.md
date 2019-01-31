---
title: Troubleshooting
nav_order: 8
has_children: true
permalink: /troubleshooting
---

# Windows

The following are Windows-specific issues.

## Python version

To specify the Python version in Windows, run:

```
virtualenv venv --python="<path/to/python3/executable>"
```

If you have multiple Python installations, here are the default locations:

* Python 2 - `C:\Python27\python.exe`
* Python 3 - `%LOCALAPPDATA%\Programs\Python\<python-version>\python.exe`
