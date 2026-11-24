from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .open_search_iam_federation_options_input import OpenSearchIAMFederationOptionsInput
from .open_search_jwt_options_input import OpenSearchJWTOptionsInput
from .open_search_master_user_options import OpenSearchMasterUserOptions
from .open_search_saml_options_input import OpenSearchSAMLOptionsInput


class OpenSearchAdvancedSecurityOptionsInput(BaseModel):
    Enabled: StrictBool | None = None
    InternalUserDatabaseEnabled: StrictBool | None = None
    MasterUserOptions: OpenSearchMasterUserOptions | None = None
    SAMLOptions: OpenSearchSAMLOptionsInput | None = None
    JWTOptions: OpenSearchJWTOptionsInput | None = None
    IAMFederationOptions: OpenSearchIAMFederationOptionsInput | None = None
    AnonymousAuthEnabled: StrictBool | None = None
