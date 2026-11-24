from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_override import ConnectHoursOfOperationOverride


class ConnectListHoursOfOperationOverridesResponse(BaseModel):
    NextToken: StrictStr | None = None
    HoursOfOperationOverrideList: list[ConnectHoursOfOperationOverride] | None = None
    LastModifiedRegion: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
