from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeleteCertificateAuthorityRequest(BaseModel):
    clusterName: StrictStr
    certificateAuthorityId: StrictStr
    clientRequestToken: StrictStr | None = None
