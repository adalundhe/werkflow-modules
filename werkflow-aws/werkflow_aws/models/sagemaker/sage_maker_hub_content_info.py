from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerHubContentInfo(BaseModel):
    HubContentName: StrictStr | None = None
    HubContentArn: StrictStr | None = None
    SageMakerPublicHubContentArn: StrictStr | None = None
    HubContentVersion: StrictStr | None = None
    HubContentType: StrictStr | None = None
    DocumentSchemaVersion: StrictStr | None = None
    HubContentDisplayName: StrictStr | None = None
    HubContentDescription: StrictStr | None = None
    SupportStatus: StrictStr | None = None
    HubContentSearchKeywords: list[StrictStr] | None = None
    HubContentStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    OriginalCreationTime: datetime.datetime | StrictStr | None = None
