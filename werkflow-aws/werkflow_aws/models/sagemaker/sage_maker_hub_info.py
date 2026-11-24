from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerHubInfo(BaseModel):
    HubName: StrictStr | None = None
    HubArn: StrictStr | None = None
    HubDisplayName: StrictStr | None = None
    HubDescription: StrictStr | None = None
    HubSearchKeywords: list[StrictStr] | None = None
    HubStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
