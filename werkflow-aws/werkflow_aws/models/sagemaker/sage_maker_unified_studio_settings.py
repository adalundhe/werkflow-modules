from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUnifiedStudioSettings(BaseModel):
    StudioWebPortalAccess: StrictStr | None = None
    DomainAccountId: StrictStr | None = None
    DomainRegion: StrictStr | None = None
    DomainId: StrictStr | None = None
    ProjectId: StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    ProjectS3Path: StrictStr | None = None
    SingleSignOnApplicationArn: StrictStr | None = None
