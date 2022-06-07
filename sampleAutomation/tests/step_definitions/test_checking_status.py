import requests
import time

from pytest_bdd import scenarios, given, then, parsers
from helpers.schemaValidation import validate_schema

from helpers.envConfig import GETURL

from step_definitions.test_a_post_getting_ID import get_job_id


scenarios("../../tests/features/GET_checking_status.feature")


@given("the user makes the GET request", target_fixture="get_response")
def make_get_request(get_job_id: int) -> requests.Response:
    print("***making GET request***")
    return requests.get(f"{GETURL}{get_job_id}")


@given(parsers.parse("the response status code should return {code:d}"))
def get_status_code(get_response: requests.Response, code: int) -> None:
    print("***checking status code for GET method***")
    assert get_response.status_code == code


@given("the status response schema should be validated")
def status_validate(get_response: requests.Response) -> None:
    print("***Validate schema for GET method***")
    validate_schema("job_get_schema.json", get_response.json())


@then("the ingest state should be present in response")
def validate_asset_state(get_response: requests.Response, get_job_id: int) -> None:
    print("***ingest status***")
    asset_response_status = get_response.json().get("assetState")
    print(f"*** JOB ID: {get_job_id}")
    while asset_response_status not in ("PUBLISHED", "FAILED"):
        print(f"Search Not yet completed,searching again..{asset_response_status}")
        time.sleep(18)  # 3minute
        _next_response = make_get_request(get_job_id)
        asset_response_status = _next_response.json().get("assetState")
    else:
        assert asset_response_status == "PUBLISHED"


@given("the user validates the analysis data of output")
def analysis_output(get_response: requests.Response) -> None:
    print("***Analysis data output***")
    analysis_response = get_response.json().get("analysisOutput")
    if len(analysis_response) >= 1:
        renditions_response = analysis_response.get("renditions")
        if len(renditions_response) > 1:
            renditions_response[0].get("format") == "video"
            renditions_response[0].get("prefix") == "u-6400-m-640x480-1000-1"
            renditions_response[1].get("format") == "audio"
            renditions_response[1].get("prefix") == "u-6400-a-128-1"
            assert len(renditions_response[0]) == len(renditions_response[1])
    else:
        print("no data")
