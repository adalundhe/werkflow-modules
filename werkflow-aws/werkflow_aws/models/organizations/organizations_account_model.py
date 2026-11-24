from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OrganizationsAccountModel(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Email: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    State: StrictStr | None = None
    Paths: list[StrictStr] | None = None
    JoinedMethod: StrictStr | None = None
    JoinedTimestamp: datetime.datetime | StrictStr | None = None
