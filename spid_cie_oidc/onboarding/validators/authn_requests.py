
from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, HttpUrl, conlist, constr

# TODO: Schema of claims is not genrated


class AcrValuesSpid(str, Enum):
    l1 = "https://www.spid.gov.it/SpidL1"
    l2 = "https://www.spid.gov.it/SpidL2"
    l3 = "https://www.spid.gov.it/SpidL3"


class AcrValuesCie(str, Enum):
    l1 = "CIE_L1"
    l2 = "CIE_L2"
    l3 = "CIE_L3"


class ScopeSpid(str, Enum):
    openid = "openid"
    offline_access = "offline_access"


class ScopeCie(str, Enum):
    openid = "openid"
    offline_access = "offline_access"
    profile = "profile"
    email = "email"


class ClaimsTypeEssential(BaseModel):
    essential: Optional[bool]


class ClaimsTypeStringValue(BaseModel):
    value: Optional[str]


class ClaimsTypeStringValues(BaseModel):
    values: Optional[conlist(str, max_items = 2, min_items = 2)]


class ClaimsType(str, Enum):
    essential = ClaimsTypeEssential
    value = ClaimsTypeStringValue
    values = ClaimsTypeStringValues


class UserInfo(BaseModel):
    given_name: Optional[dict]
    family_name: Optional[dict]
    email: Optional[dict]
    email_verified: Optional[dict]
    gender: Optional[dict]
    birthdate: Optional[dict]
    phone_number: Optional[dict]
    phone_number_verified: Optional[dict]
    address: Optional[dict]
    place_of_birth: Optional[dict]
    document_details: Optional[dict]
    e_delivery_service: Optional[dict]
    fiscal_number: Optional[dict]
    physical_phone_number: Optional[dict]


class IdToken(UserInfo):
    pass


TYPES = {
    'essential': ClaimsTypeEssential,
    'value': ClaimsTypeStringValue,
    'values': ClaimsTypeStringValues,
}

CLAIMS_SPID = {
    'userinfo': UserInfo
}

CLAIMS_CIE = {
    'userinfo': UserInfo,
    'id_token': IdToken
}


class AuthenticationRequest(BaseModel):
    client_id: HttpUrl
    response_type: Literal['code']
    code_challenge: str
    code_challenge_method: Literal['S256']
    nonce: constr(min_length = 32)
    redirect_uri: HttpUrl
    claims : Optional[dict]
    state: constr(min_length = 32)
    # TODO: to be improved
    ui_locales: Optional[List[str]]


def validate_message(msg:dict, cl:dict) -> None:
    claims = msg['claims']
    for k_claim,v_claim in claims.items():
        claims_items = cl.get(k_claim, None)
        if not claims_items:
            continue
        claims_items(**v_claim)
        for k_item, v_item in v_claim.items():
            if v_item is not None:
                for k_type, v_type in TYPES.items():
                    v_type(**v_item)


class AuthenticationRequestSpid(AuthenticationRequest):
    # TODO: openid must be mandatory
    scope: List[ScopeSpid]
    prompt: Literal['consent', 'consent login', 'verify']
    acr_values: List[AcrValuesSpid]

    def get_claims() -> dict:
        return CLAIMS_SPID


class AuthenticationRequestCie(AuthenticationRequest):
    # TODO: openid must be mandatory
    scope: List[ScopeCie]
    prompt: Literal['consent', 'consent login']
    acr_values: List[AcrValuesCie]

    def get_claims() -> dict:
        return CLAIMS_CIE
