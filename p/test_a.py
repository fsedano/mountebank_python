import requests
from hamcrest import assert_that
from brunns.matchers.response import is_response
from mbtest.matchers import had_request
from mbtest.imposters import Imposter, Predicate, Response, Stub

def test_request_to_mock_server(mock_server):
    # Set up mock server with required behavior
    imposter = Imposter(
            Stub(
                Predicate(path="/login_data"), 
                Response(body={'authz':True})
            ),
            record_requests=True,
            port=8080)

    with mock_server(imposter) as ms:
        # Call our service
        #response = requests.get(f"{imposter.url}/test")
        response = requests.get("http://dut:5000/login")
        #print(response.json())
        assert response.json() == {'authz':True}
        #assert_that(response, is_response().with_status_code(200))
        #assert_that(imposter, had_request().with_path("/login_data").and_method("GET"))

        