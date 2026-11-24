from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSCreateCertificateAuthorityRequest(BaseModel):
    clusterName: StrictStr
    clientRequestToken: StrictStr | None = None
