from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubDisruptionCompliance(BaseModel):
    achievableRpoInSecs: StrictInt | None = None
    achievableRtoInSecs: StrictInt | None = None
    complianceStatus: StrictStr | None = None
    currentRpoInSecs: StrictInt | None = None
    currentRtoInSecs: StrictInt | None = None
    message: StrictStr | None = None
    rpoDescription: StrictStr | None = None
    rpoReferenceId: StrictStr | None = None
    rtoDescription: StrictStr | None = None
    rtoReferenceId: StrictStr | None = None
