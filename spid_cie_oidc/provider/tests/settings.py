
op_conf = {
    'sub': 'http://op-test/oidc/op/',
    'default_exp': 2880,
    'default_signature_alg': 'RS256',
    'authority_hints': ['http://op-test/oidc/op/'],
    'jwks': [
        {'kty': 'RSA',
        'kid': 'dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw',
        'n': '01_4aI2Lu5ggsElmRkE_S_a83V_szXU0txV4db2hmJ8HR1Y2s7PsZZ5-emGpnTydGrR3n-QExeEEIcFt_a06Ryiink34RQcKoGXUDBMBU0Bu8G7NcZ99YX6yeG9wFi4xs-WviTPmtPqijkz6jm1_ltWDcwbktfkraIRKKggZaEl9ldtsFr2wSpin3AXuGIdeJ0hZqhF92ODBLGjJlaIL9KlwopDy56adReVnraawSdrxmuPGj78IEADNAme2nQNvv9UCu0FkAn5St1bKds3Gpv26W0kjr1gZLsmQrj9lTcDk_KbAwfEY__P7se62kusoSuKMTQqUG1TQpUY7oFGSdw',
        'e': 'AQAB',
        'd': 'AxvyR3dtisDeGjm6K2ZiS_fBJ3B1xz_mGptSPkkfy2LrdH0sKNCItaXzLlGpcQqnNPFaoRt1hoOcz_JMb-LQbKOIYNO8xycnXNyildrhthvIhfjbRMSXz4tRjLv25hyf1omWX2pIBnl5UqaHOPkbW1igqlx7mMGlhdAMVznvRb1oJOXxPtSdlVOhqT5ohn4BJZcJ85TKm_E49KUKUsz_xkd3BlYnUaiuEu-VQbC0u61iH-N017wg4ZQn9eXQgAzFdSNI2GQ7IH76l00iUu-y9oT2ld4WHGYMmsZBJgaQZnu2Yj4IMb5NjQz2VAOTU844RXP7-7Y5rWsS1oewfWSHAQ',
        'p': '9dvm96S4wBrwzs73DOG8eV6sWEN13ZJNLa4tKzJvonOLG_8Z9Rshnfg_HcYDm_mqRD-nFC-8JKufnNaZbZuO_hDiA6UkvlZMGePxoN7nueHGfAqZ9lRQX0Vpp2Ac480jJgBLOhwgjkySRI5Ck-enTGabkxVN_LJSU9FC54TW6KE',
        'q': '3BfwsumO62vhekd2gm97Uk1XFOM5UXmb1esdFnZ_RZRw1tDUB2irTxLJSqECCZbMWRoFRB3k-17LAOMaITUqv8g-83zdCmR3gpO71ahbdEfkGGKQYL7WmMNv3YvSMY5lN4_mCEz8R_OCz0_H7bip0Es_KAl5TSXjnVTvaACnLBc'
        }
    ],
    'trust_marks': [],
    'trust_marks_issuers': {},
    'entity_type': 'openid_provider',
    'metadata': {
        'openid_provider': {
            'authorization_endpoint': 'http://op-test/oidc/op/authorization',
            'token_endpoint': 'http://op-test/oidc/op/token',
            'userinfo_endpoint': 'http://op-test/oidc/op/userinfo',
            'introspection_endpoint': 'http://op-test/oidc/op/introspection',
            'claims_parameter_supported': True,
            'contacts': ['ops@https://idp.it'],
            'client_registration_types_supported': ['automatic'],
            'request_authentication_methods_supported': {'ar': ['request_object']},
            'acr_values_supported': [
                'https://www.spid.gov.it/SpidL1',
                'https://www.spid.gov.it/SpidL2',
                'https://www.spid.gov.it/SpidL3'
            ],
            'claims_supported': [
                'https://attributes.spid.gov.it/spidCode',
                'https://attributes.spid.gov.it/name',
                'https://attributes.spid.gov.it/familyName',
                'https://attributes.spid.gov.it/placeOfBirth',
                'https://attributes.spid.gov.it/countyOfBirth',
                'https://attributes.spid.gov.it/dateOfBirth',
                'https://attributes.spid.gov.it/gender',
                'https://attributes.spid.gov.it/companyName',
                'https://attributes.spid.gov.it/registeredOffice',
                'https://attributes.spid.gov.it/fiscalNumber',
                'https://attributes.spid.gov.it/ivaCode',
                'https://attributes.spid.gov.it/idCard',
                'https://attributes.spid.gov.it/mobilePhone',
                'https://attributes.spid.gov.it/email',
                'https://attributes.spid.gov.it/address',
                'https://attributes.spid.gov.it/expirationDate',
                'https://attributes.spid.gov.it/digitalAddress'
            ],
            'grant_types_supported': ['authorization_code', 'refresh_token'],
            'id_token_signing_alg_values_supported': ['RS256', 'ES256'],
            'issuer': 'http://op-test/oidc/op/',
            'jwks': {
                'keys': 
                [
                    {
                        'kty': 'RSA',
                        'n': '01_4aI2Lu5ggsElmRkE_S_a83V_szXU0txV4db2hmJ8HR1Y2s7PsZZ5-emGpnTydGrR3n-QExeEEIcFt_a06Ryiink34RQcKoGXUDBMBU0Bu8G7NcZ99YX6yeG9wFi4xs-WviTPmtPqijkz6jm1_ltWDcwbktfkraIRKKggZaEl9ldtsFr2wSpin3AXuGIdeJ0hZqhF92ODBLGjJlaIL9KlwopDy56adReVnraawSdrxmuPGj78IEADNAme2nQNvv9UCu0FkAn5St1bKds3Gpv26W0kjr1gZLsmQrj9lTcDk_KbAwfEY__P7se62kusoSuKMTQqUG1TQpUY7oFGSdw',
                        'e': 'AQAB',
                        'kid': 'dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw'
                    }
                ]
            },
            'scopes_supported': ['openid', 'offline_access'],
            'logo_uri': 'http://op-test/oidc/op/statics/logo.svg',
            'organization_name': 'SPID OIDC identity provider',
            'op_policy_uri': 'http://op-test/oidc/op/en/website/legal-information/',
            'request_parameter_supported': True,
            'request_uri_parameter_supported': True,
            'require_request_uri_registration': True,
            'response_types_supported': ['code'],
            'subject_types_supported': ['pairwise', 'public'],
            'token_endpoint_auth_methods_supported': ['private_key_jwt'],
            'token_endpoint_auth_signing_alg_values_supported': [
                'RS256',
                'RS384',
                'RS512',
                'ES256',
                'ES384',
                'ES512'
            ],
            'userinfo_encryption_alg_values_supported': [
                'RSA-OAEP',
                'RSA-OAEP-256',
                'ECDH-ES',
                'ECDH-ES+A128KW',
                'ECDH-ES+A192KW',
                'ECDH-ES+A256KW'
            ],
            'userinfo_encryption_enc_values_supported': [
                'A128CBC-HS256',
                'A192CBC-HS384',
                'A256CBC-HS512',
                'A128GCM',
                'A192GCM',
                'A256GCM'
            ],
            'userinfo_signing_alg_values_supported': [
                'RS256',
                'RS384',
                'RS512',
                'ES256',
                'ES384',
                'ES512'
            ],
            'request_object_encryption_alg_values_supported': [
                'RSA-OAEP',
                'RSA-OAEP-256',
                'ECDH-ES',
                'ECDH-ES+A128KW',
                'ECDH-ES+A192KW',
                'ECDH-ES+A256KW'
            ],
            'request_object_encryption_enc_values_supported': [
                'A128CBC-HS256',
                'A192CBC-HS384',
                'A256CBC-HS512',
                'A128GCM',
                'A192GCM',
                'A256GCM'
            ],
            'request_object_signing_alg_values_supported': ['RS256',
                'RS384',
                'RS512',
                'ES256',
                'ES384',
                'ES512'
            ]
        }
    },
    'constraints': {},
    'is_active': True
}