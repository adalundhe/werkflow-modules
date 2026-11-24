from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_config import ConnectHoursOfOperationConfig
from .connect_hours_of_operations_identifier import ConnectHoursOfOperationsIdentifier


class ConnectHoursOfOperation(BaseModel):
    HoursOfOperationId: StrictStr | None = None
    HoursOfOperationArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    TimeZone: StrictStr | None = None
    Config: list[ConnectHoursOfOperationConfig] | None = None
    ParentHoursOfOperations: list[ConnectHoursOfOperationsIdentifier] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
