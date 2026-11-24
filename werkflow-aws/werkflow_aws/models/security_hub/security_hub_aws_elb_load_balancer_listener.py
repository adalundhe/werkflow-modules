from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsElbLoadBalancerListener(BaseModel):
    InstancePort: StrictInt | None = None
    InstanceProtocol: StrictStr | None = None
    LoadBalancerPort: StrictInt | None = None
    Protocol: StrictStr | None = None
    SslCertificateId: StrictStr | None = None
