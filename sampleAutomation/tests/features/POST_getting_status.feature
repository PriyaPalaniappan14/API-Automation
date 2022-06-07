Feature: API testing
    Scenario: Making POST request
        Given we have a valid payload
        When the user makes a POST request
        Then the response status code should return 200
        And the job response schema should be validated
        Then the jobID should be present in response
        Then the user validates the job id







