from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRSessionMappingDetail(BaseModel):
    StudioId: StrictStr | None = None
    IdentityId: StrictStr | None = None
    IdentityName: StrictStr | None = None
    IdentityType: StrictStr | None = None
    SessionPolicyArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
