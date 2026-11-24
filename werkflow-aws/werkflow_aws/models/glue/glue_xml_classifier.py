from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GlueXMLClassifier(BaseModel):
    Name: StrictStr | None = None
    Classification: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    RowTag: StrictStr | None = None
