import pytest
import requests
from typing import Optional
from pytest_bdd import given, when, then

# Hooks
def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception
):
    print(f"Step failed: {step}")


# Global dictionary for storing data for POST and GET endpoint
generic_storage: dict = {}
