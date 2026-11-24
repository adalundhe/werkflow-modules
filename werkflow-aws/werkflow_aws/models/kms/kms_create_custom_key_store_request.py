from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kms_xks_proxy_authentication_credential_type import KMSXksProxyAuthenticationCredentialType


class KMSCreateCustomKeyStoreRequest(BaseModel):
    CustomKeyStoreName: StrictStr
    CloudHsmClusterId: StrictStr | None = None
    TrustAnchorCertificate: StrictStr | None = None
    KeyStorePassword: StrictStr | None = None
    CustomKeyStoreType: Literal['AWS_CLOUDHSM', 'EXTERNAL_KEY_STORE'] | None = None
    XksProxyUriEndpoint: StrictStr | None = None
    XksProxyUriPath: StrictStr | None = None
    XksProxyVpcEndpointServiceName: StrictStr | None = None
    XksProxyVpcEndpointServiceOwner: StrictStr | None = None
    XksProxyAuthenticationCredential: KMSXksProxyAuthenticationCredentialType | None = None
    XksProxyConnectivity: Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE'] | None = None
