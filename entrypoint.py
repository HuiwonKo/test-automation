import pytest


retcode = pytest.main(["-x", "tests"])
print("retcode***", int(retcode))
# 0 : all tests passed, 1 : failed

# https://stackoverflow.com/questions/3343205/how-to-use-pytest-from-python
