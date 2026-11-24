from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AcmeExternalAccountBindingSummary(BaseModel):
    AcmeExternalAccountBindingArn: StrictStr | None = None
    AcmeEndpointArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
    RevokedAt: datetime.datetime | StrictStr | None = None
    LastUsedAt: datetime.datetime | StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
