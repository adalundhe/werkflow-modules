from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GlueJsonClassifier(BaseModel):
    Name: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    JsonPath: StrictStr | None = None
