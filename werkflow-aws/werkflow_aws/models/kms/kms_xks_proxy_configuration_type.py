from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSXksProxyConfigurationType(BaseModel):
    Connectivity: StrictStr | None = None
    AccessKeyId: StrictStr | None = None
    UriEndpoint: StrictStr | None = None
    UriPath: StrictStr | None = None
    VpcEndpointServiceName: StrictStr | None = None
    VpcEndpointServiceOwner: StrictStr | None = None
