from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCreatePresignedDomainUrlRequest(BaseModel):
    DomainId: StrictStr
    UserProfileName: StrictStr
    SessionExpirationDurationInSeconds: StrictInt | None = None
    ExpiresInSeconds: StrictInt | None = None
    SpaceName: StrictStr | None = None
    LandingUri: StrictStr | None = None
