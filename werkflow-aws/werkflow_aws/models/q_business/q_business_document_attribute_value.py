from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessDocumentAttributeValue(BaseModel):
    stringValue: StrictStr | None = None
    stringListValue: list[StrictStr] | None = None
    longValue: StrictInt | None = None
    dateValue: datetime.datetime | StrictStr | None = None
