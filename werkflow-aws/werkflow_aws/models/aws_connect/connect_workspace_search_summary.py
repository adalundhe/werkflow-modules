from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectWorkspaceSearchSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Visibility: StrictStr | None = None
    Description: StrictStr | None = None
    Title: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
