from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueUsageProfileDefinition(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
