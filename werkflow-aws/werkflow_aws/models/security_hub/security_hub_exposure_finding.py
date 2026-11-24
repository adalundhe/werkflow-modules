from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubExposureFinding(BaseModel):
    MetadataUid: StrictStr | None = None
    Title: StrictStr | None = None
    PreviousSeverity: StrictStr | None = None
    ProjectedSeverity: StrictStr | None = None
    Impact: StrictStr | None = None
