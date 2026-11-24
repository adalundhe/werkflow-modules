from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamUser(BaseModel):
    Arn: StrictStr | None = None
    UserName: StrictStr | None = None
    Enabled: StrictBool | None = None
    Status: StrictStr | None = None
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    AuthenticationType: StrictStr | None = None
