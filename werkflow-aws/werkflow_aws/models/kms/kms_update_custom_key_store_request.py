from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kms_xks_proxy_authentication_credential_type import KMSXksProxyAuthenticationCredentialType


class KMSUpdateCustomKeyStoreRequest(BaseModel):
    CustomKeyStoreId: StrictStr
    NewCustomKeyStoreName: StrictStr | None = None
    KeyStorePassword: StrictStr | None = None
    CloudHsmClusterId: StrictStr | None = None
    XksProxyUriEndpoint: StrictStr | None = None
    XksProxyUriPath: StrictStr | None = None
    XksProxyVpcEndpointServiceName: StrictStr | None = None
    XksProxyVpcEndpointServiceOwner: StrictStr | None = None
    XksProxyAuthenticationCredential: KMSXksProxyAuthenticationCredentialType | None = None
    XksProxyConnectivity: Literal['PUBLIC_ENDPOINT', 'VPC_ENDPOINT_SERVICE'] | None = None
