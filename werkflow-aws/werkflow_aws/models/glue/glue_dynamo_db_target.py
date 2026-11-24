from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class GlueDynamoDBTarget(BaseModel):
    Path: StrictStr | None = None
    scanAll: StrictBool | None = None
    scanRate: StrictFloat | StrictInt | None = None
