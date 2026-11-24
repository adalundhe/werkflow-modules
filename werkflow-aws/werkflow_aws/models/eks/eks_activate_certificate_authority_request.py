from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSActivateCertificateAuthorityRequest(BaseModel):
    clusterName: StrictStr
    certificateAuthorityId: StrictStr
    clientRequestToken: StrictStr | None = None
