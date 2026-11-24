from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectTaskTemplateMetadata(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
