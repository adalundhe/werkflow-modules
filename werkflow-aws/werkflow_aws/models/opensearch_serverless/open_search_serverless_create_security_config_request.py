from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_serverless_create_iam_identity_center_config_options import OpenSearchServerlessCreateIamIdentityCenterConfigOptions
from .open_search_serverless_iam_federation_config_options import OpenSearchServerlessIamFederationConfigOptions
from .open_search_serverless_saml_config_options import OpenSearchServerlessSamlConfigOptions


class OpenSearchServerlessCreateSecurityConfigRequest(BaseModel):
    type: Literal['saml', 'iamidentitycenter', 'iamfederation']
    name: StrictStr
    description: StrictStr | None = None
    samlOptions: OpenSearchServerlessSamlConfigOptions | None = None
    iamIdentityCenterOptions: OpenSearchServerlessCreateIamIdentityCenterConfigOptions | None = None
    iamFederationOptions: OpenSearchServerlessIamFederationConfigOptions | None = None
    clientToken: StrictStr | None = None
