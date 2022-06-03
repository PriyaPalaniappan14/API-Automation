Feature: Transcoder Implementation

    Background:
        Given the user makes the GET request
        And the response status code should return 200

    Scenario: Making the GET Request
        Given the status response schema should be validated
        Then the ingest state should be present in response
    @skip
    Scenario: Checking analysis output response
        Given the user validates the analysis data of output



