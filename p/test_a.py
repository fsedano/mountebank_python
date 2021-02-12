import requests
from hamcrest import assert_that
from brunns.matchers.response import is_response
from mbtest.matchers import had_request
from mbtest.imposters import Imposter, Predicate, Response, Stub

def test_request_to_mock_server(mock_server):
    # Set up mock server with required behavior
    imposter = Imposter(
            Stub(
                Predicate(path="/test"), 
                Response(body="sausages")
            ),
            record_requests=True,
            port=8080)

    with mock_server(imposter) as ms:
        # Make request to mock server - exercise code under test here
        response = requests.get(f"{imposter.url}/test")
        print(ms.get_actual_requests())
        assert_that(response, is_response().with_status_code(200).and_body("sausages"))
        assert_that(imposter, had_request().with_path("/test").and_method("GET"))

        