from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerUserProfileDetails(BaseModel):
    DomainId: StrictStr | None = None
    UserProfileName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
