from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_iam_federation_config_options import OpenSearchServerlessIamFederationConfigOptions
from .open_search_serverless_iam_identity_center_config_options import OpenSearchServerlessIamIdentityCenterConfigOptions
from .open_search_serverless_saml_config_options import OpenSearchServerlessSamlConfigOptions


class OpenSearchServerlessSecurityConfigDetail(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
    configVersion: StrictStr | None = None
    description: StrictStr | None = None
    samlOptions: OpenSearchServerlessSamlConfigOptions | None = None
    iamIdentityCenterOptions: OpenSearchServerlessIamIdentityCenterConfigOptions | None = None
    iamFederationOptions: OpenSearchServerlessIamFederationConfigOptions | None = None
    createdDate: StrictInt | None = None
    lastModifiedDate: StrictInt | None = None
