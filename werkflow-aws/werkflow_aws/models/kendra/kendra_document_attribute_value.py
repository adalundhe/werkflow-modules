from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class KendraDocumentAttributeValue(BaseModel):
    StringValue: StrictStr | None = None
    StringListValue: list[StrictStr] | None = None
    LongValue: StrictInt | None = None
    DateValue: datetime.datetime | StrictStr | None = None
