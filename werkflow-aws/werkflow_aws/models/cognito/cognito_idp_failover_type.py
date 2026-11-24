from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPFailoverType(BaseModel):
    SecondaryRegion: StrictStr | None = None
    PrimaryRoute53HealthCheckId: StrictStr | None = None
