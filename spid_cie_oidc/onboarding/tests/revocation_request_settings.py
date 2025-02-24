from copy import deepcopy

REVOCATION_REQUEST = {
    "client_assertion": "eyJhbGciOiJIUzpXVCJ9.eyJzdWIdHJ1ZX0.LVyRDPVJm0S9q",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_id": "https://rp.spid.agid.gov.it",
    "token" : "eyJhbGciOiJSUzI1NiJ9.eyR9.FXDtEzDLbTHzFNroW7w27RLk"
}

REVOCATION_REQUEST_NO_CLIENT_ASSERTION = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CLIENT_ASSERTION.pop("client_assertion")

REVOCATION_REQUEST_NO_CORRECT_CLIENT_ASSERTION = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CORRECT_CLIENT_ASSERTION["client_assertion"] = ".payload."

REVOCATION_REQUEST_NO_CLIENT_ASSERTION_TYPE = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CLIENT_ASSERTION_TYPE.pop("client_assertion_type")

REVOCATION_REQUEST_NO_CORRECT_CLIENT_ASSERTION_TYPE = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CORRECT_CLIENT_ASSERTION_TYPE["client_assertion_type"] = ""

REVOCATION_REQUEST_NO_CLIENT_ID = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CLIENT_ID.pop("client_id")

REVOCATION_REQUEST_NO_CORRECT_CLIENT_ID = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CORRECT_CLIENT_ID["client_id"] = ""

REVOCATION_REQUEST_NO_TOKEN = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_TOKEN.pop("token")

REVOCATION_REQUEST_NO_CORRECT_TOKEN = deepcopy(REVOCATION_REQUEST)
REVOCATION_REQUEST_NO_CORRECT_TOKEN["token"] = ".."
