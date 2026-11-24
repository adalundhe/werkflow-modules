from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFrontFunctionMetadata(BaseModel):
    FunctionARN: StrictStr | None = None
    Stage: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
