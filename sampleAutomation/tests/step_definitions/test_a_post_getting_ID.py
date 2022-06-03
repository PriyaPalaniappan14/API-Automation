from typing import Dict
import requests
import pytest
import logging

from pytest_bdd import scenarios, given, then, when, parsers

from helpers.envConfig import POST_ENDPOINT, HEADER_REQUEST
from helpers.postPayload import create_make_job_payload
from helpers.schemaValidation import validate_schema

from .conftest import generic_storage

scenarios("../../tests/features/POST_getting_status.feature")


@given("we have a valid payload", target_fixture="post_payload")
def create_valid_payload() -> str:
    print("***Creating payload***")
    return create_make_job_payload()


@when("the user makes a POST request")
def make_post_request(post_payload) -> requests.Response:
    print("***making post request***")
    generic_storage["stored_response"] = requests.post(
        POST_ENDPOINT, headers=HEADER_REQUEST, data=post_payload
    )


@then(parsers.parse("the response status code should return {code:d}"))
def validate_response_status(
    post_response: requests.Response,
    code: int,
) -> None:
    print("***validate status***")
    assert post_response.status_code == code


@then("the job response schema should be validated")
def validate_job_response_schema(post_response: requests.Response) -> requests.Response:
    print("***validating schema***")
    validate_schema("job_post_schema.json", post_response.json())


@then("the jobID should be present in response")
def get_job_id(post_response: requests.Response) -> int:
    print("***Getting job ID from post response***")
    post_json_obj = post_response.json()
    assert "id" in post_json_obj
    getting_job_id = post_json_obj.get("id")
    return getting_job_id


@then("the user validates the job id")
def params_id(post_response: requests.Response) -> int:
    print("***Job ID sends to GET Method***")
    generic_storage["job_value"] = post_response.json()["id"]


@pytest.fixture
def post_response() -> requests.Response:
    return generic_storage["stored_response"]


@pytest.fixture
def get_job_id() -> int:
    return generic_storage["job_value"]
