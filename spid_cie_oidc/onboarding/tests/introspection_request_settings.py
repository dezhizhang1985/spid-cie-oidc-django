from copy import deepcopy

INTROSPECTION_REQUEST = {
    "client_assertion": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI.LVyRDPVJ",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_id": "https://rp.spid.agid.gov.it",
    "token": "eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTQsImF1ZCI6W.FXDtEzDL"
}

INTROSPECTION_REQUEST_NO_CLIENT_ASSERTION = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CLIENT_ASSERTION.pop("client_assertion")

INTROSPECTION_REQUEST_NO_CORRECT_CLIENT_ASSERTION = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CORRECT_CLIENT_ASSERTION["client_assertion"] = ".payload.sig"

INTROSPECTION_REQUEST_NO_CLIENT_ASSERTION_TYPE = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CLIENT_ASSERTION_TYPE.pop("client_assertion_type")

INTROSPECTION_REQUEST_NO_CORRECT_CLIENT_ASSERTION_TYPE = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CORRECT_CLIENT_ASSERTION_TYPE["client_assertion_type"] = ""

INTROSPECTION_REQUEST_NO_CLIENT_ID = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CLIENT_ID.pop("client_id")

INTROSPECTION_REQUEST_NO_CORRECT_CLIENT_ID = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CORRECT_CLIENT_ID["client_id"] = "https//rp.spid.agid.gov.it"

INTROSPECTION_REQUEST_NO_TOKEN = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_TOKEN.pop("token")

INTROSPECTION_REQUEST_NO_CORRECT_TOKEN = deepcopy(INTROSPECTION_REQUEST)
INTROSPECTION_REQUEST_NO_CORRECT_TOKEN["token"] = ".sign"