from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operations_identifier import ConnectHoursOfOperationsIdentifier


class ConnectListChildHoursOfOperationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ChildHoursOfOperationsSummaryList: list[ConnectHoursOfOperationsIdentifier] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
