from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_action_connector_error import QuickSightActionConnectorError


class QuickSightActionConnectorSummary(BaseModel):
    Arn: StrictStr | None = None
    ActionConnectorId: StrictStr | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Error: QuickSightActionConnectorError | None = None
