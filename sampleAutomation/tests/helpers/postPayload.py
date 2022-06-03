"""
This contains helper functions for creating post payloads
"""

from helpers.common import (
    load_json_as_string,
    get_data_file,
)


def create_make_job_payload() -> str:
    """
    Load the create job payload from the data directory
    """
    return load_json_as_string(get_data_file("payloads/job_post_payload.json"))
