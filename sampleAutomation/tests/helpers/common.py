import os
import json

# from step_definitions.test_requestAPI import test_gettingId


class YospaceQAException(Exception):
    pass


def get_data_file(filename: str) -> str:
    _absolute_path = os.path.dirname(os.path.abspath(__file__))
    _relative_path = os.path.join(_absolute_path, "..", "data/")
    _data_path = os.path.abspath(os.path.dirname(_relative_path))
    return os.path.join(_data_path, filename)


def load_json_as_dict(filename: str) -> dict:
    _return_dict: dict = {}

    with open(filename, "r", encoding="utf-8") as json_file:
        _return_dict = json.load(json_file)

    return _return_dict


def load_json_as_string(filename: str) -> str:
    """
    Loads a JSON file using the filename provided and
    returns its contents as a string (dict to str)
    """
    return json.dumps(load_json_as_dict(filename))


"""
def test_createJobId():
    postCreateJob = requests.post(POST_ENDPOINT, headers = headerRequest, data = postPayload)
    return postCreateJob

    
@pytest.fixture
def getMethod(createJobId):
    createJobResponse = createJobId.json()
    getMethod = requests.get(GETURL, params = createJobResponse['id'])
    return getMethod
"""
