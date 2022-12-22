### Hexlet tests and linter status:
[![Actions Status](https://github.com/MortInsane/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/MortInsane/python-project-50/actions)
[![Mort CI](https://github.com/MortInsane/python-project-50/actions/workflows/mort-CI.yml/badge.svg)](https://github.com/MortInsane/python-project-50/actions/workflows/mort-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/5230ddf9afc45b8235c3/maintainability)](https://codeclimate.com/github/MortInsane/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5230ddf9afc45b8235c3/test_coverage)](https://codeclimate.com/github/MortInsane/python-project-50/test_coverage)

### Console application
> **Difference Calculator** – *a program that determines the difference between two data structures.*
Support formats: **json**, **yaml**

### Installation
```bash
git clone git@github.com:MortInsane/python-project-50.git
cd python-project-50

make package-build
make package-install
```

### Use app
```bash
STYLISH:
gendiff path1.json/yaml/yml path2.json/yaml/yml -f stylish or
gendiff path1.json/yaml/yml path2.json/yaml/yml

PLAIN:
gendiff path1.json/yaml/yml path2.json/yaml/yml -f plain

JSON:
gendiff path1.json/yaml/yml path2.json/yaml/yml -f json
```

### Preview
[![asciicast](https://asciinema.org/a/547313.svg)](https://asciinema.org/a/547313)