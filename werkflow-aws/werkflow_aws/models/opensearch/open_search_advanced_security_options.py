from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_iam_federation_options_output import OpenSearchIAMFederationOptionsOutput
from .open_search_jwt_options_output import OpenSearchJWTOptionsOutput
from .open_search_saml_options_output import OpenSearchSAMLOptionsOutput


class OpenSearchAdvancedSecurityOptions(BaseModel):
    Enabled: StrictBool | None = None
    InternalUserDatabaseEnabled: StrictBool | None = None
    SAMLOptions: OpenSearchSAMLOptionsOutput | None = None
    JWTOptions: OpenSearchJWTOptionsOutput | None = None
    IAMFederationOptions: OpenSearchIAMFederationOptionsOutput | None = None
    AnonymousAuthDisableDate: datetime.datetime | StrictStr | None = None
    AnonymousAuthEnabled: StrictBool | None = None
