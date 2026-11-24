from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGrokClassifier(BaseModel):
    Name: StrictStr | None = None
    Classification: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    GrokPattern: StrictStr | None = None
    CustomPatterns: StrictStr | None = None
