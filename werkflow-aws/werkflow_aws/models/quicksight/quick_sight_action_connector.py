from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_action_connector_error import QuickSightActionConnectorError
from .quick_sight_read_auth_config import QuickSightReadAuthConfig


class QuickSightActionConnector(BaseModel):
    Arn: StrictStr | None = None
    ActionConnectorId: StrictStr | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Error: QuickSightActionConnectorError | None = None
    Description: StrictStr | None = None
    AuthenticationConfig: QuickSightReadAuthConfig | None = None
    EnabledActions: list[StrictStr] | None = None
    VpcConnectionArn: StrictStr | None = None
