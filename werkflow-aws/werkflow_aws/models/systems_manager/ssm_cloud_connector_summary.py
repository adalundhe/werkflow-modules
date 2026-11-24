from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMCloudConnectorSummary(BaseModel):
    CloudConnectorId: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Provider: StrictStr | None = None
    ConfigConnectorArn: StrictStr | None = None
