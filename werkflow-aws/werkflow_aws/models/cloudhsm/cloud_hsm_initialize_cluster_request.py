from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMInitializeClusterRequest(BaseModel):
    ClusterId: StrictStr
    SignedCert: StrictStr
    TrustAnchor: StrictStr
