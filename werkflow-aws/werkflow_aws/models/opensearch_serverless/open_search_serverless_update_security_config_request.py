from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_iam_federation_config_options import OpenSearchServerlessIamFederationConfigOptions
from .open_search_serverless_saml_config_options import OpenSearchServerlessSamlConfigOptions
from .open_search_serverless_update_iam_identity_center_config_options import OpenSearchServerlessUpdateIamIdentityCenterConfigOptions


class OpenSearchServerlessUpdateSecurityConfigRequest(BaseModel):
    id: StrictStr
    configVersion: StrictStr
    description: StrictStr | None = None
    samlOptions: OpenSearchServerlessSamlConfigOptions | None = None
    iamIdentityCenterOptionsUpdates: OpenSearchServerlessUpdateIamIdentityCenterConfigOptions | None = None
    iamFederationOptions: OpenSearchServerlessIamFederationConfigOptions | None = None
    clientToken: StrictStr | None = None
