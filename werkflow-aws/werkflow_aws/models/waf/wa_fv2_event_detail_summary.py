from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .wa_fv2_api_security_event_detail import WAFv2ApiSecurityEventDetail


class WAFv2EventDetailSummary(BaseModel):
    EventId: StrictStr | None = None
    EventStatus: StrictStr | None = None
    EventCategory: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ResourceArn: StrictStr | None = None
    WebAclArn: StrictStr | None = None
    ApiSecurityEventDetail: WAFv2ApiSecurityEventDetail | None = None
