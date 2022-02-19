import logging

from django.test import TestCase
from pydantic import ValidationError
from spid_cie_oidc.onboarding.validators.authn_requests import (
    AuthenticationRequestCie, AuthenticationRequestSpid, validate_message)

from .authn_request_settings import (AUTHN_REQUEST_CIE, AUTHN_REQUEST_SPID,
                                     AUTHN_REQUEST_SPID_NO_CLIENT_ID,
                                     AUTHN_REQUEST_SPID_NO_CORRECT_CLAIMS)

logger = logging.getLogger(__name__)

class AuthRequestTest(TestCase):

    def validate_spid(self):
        AuthenticationRequestSpid(**AUTHN_REQUEST_SPID)
        validate_message(AUTHN_REQUEST_SPID, AuthenticationRequestSpid.get_claims())

    def validate_spid_no_client_id(self):
        AuthenticationRequestSpid(**AUTHN_REQUEST_SPID_NO_CLIENT_ID) 
        validate_message(AUTHN_REQUEST_SPID_NO_CLIENT_ID, AuthenticationRequestSpid.get_claims())

    def validate_spid_no_correct_claims(self):
        AuthenticationRequestSpid(**AUTHN_REQUEST_SPID_NO_CORRECT_CLAIMS) 
        validate_message(AUTHN_REQUEST_SPID_NO_CORRECT_CLAIMS, AuthenticationRequestSpid.get_claims())
    
    def validate_cie(self):
        AuthenticationRequestCie(**AUTHN_REQUEST_CIE)
        validate_message(AUTHN_REQUEST_CIE, AuthenticationRequestCie.get_claims())

# logger.info(AuthenticationRequestSpid.schema_json(indent=2))
# logger.info(AuthenticationRequestCie.schema_json(indent=2))
auth_request_test = AuthRequestTest()
auth_request_test.validate_spid()
logger.info("AUTHN REQUEST SPID CHECK PASSED")
auth_request_test.validate_cie()
logger.info("AUTHN REQUEST CIE CHECK PASSED")
with auth_request_test.assertRaises(ValidationError):
    auth_request_test.validate_spid_no_client_id()
logger.info("AUTHN REQUEST SPID NO CLIENT_ID CHECK PASSED")
with auth_request_test.assertRaises(ValidationError):
    auth_request_test.validate_spid_no_correct_claims()
logger.info("AUTHN REQUEST SPID NO CORRECT CLAIMS CHECK PASSED")
        

        
