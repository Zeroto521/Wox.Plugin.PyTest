# Wox.Plugin.PyTest

Test Python language in Wox plugin, record some information to local replace `print` function.

[![Build Status](https://travis-ci.com/Zeroto521/Wox.Plugin.PyTest.svg?token=QsyzHs7fsxMnxCs5Thps&branch=master)](https://travis-ci.com/Zeroto521/Wox.Plugin.PyTest) [![codecov](https://codecov.io/gh/Zeroto521/Wox.Plugin.PyTest/branch/master/graph/badge.svg?token=FeJvDXSKxT)](https://codecov.io/gh/Zeroto521/Wox.Plugin.PyTest)

![](/images/demo.png)

## Installation

```bash
>>> git clone https://github.com/Zeroto521/Wox.Plugin.PyTest.git
>>> python setup.py install
```

## Examples

```python
>>> from pytest import testit
>>> testit('Somewords are here.')  # It will log `Somewords are here.` to local file.
```

## License

MIT License. [@Zeroto521](https://github.com/Zeroto521)
