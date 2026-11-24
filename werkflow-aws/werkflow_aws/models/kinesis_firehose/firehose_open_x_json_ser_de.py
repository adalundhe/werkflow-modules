from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FirehoseOpenXJsonSerDe(BaseModel):
    ConvertDotsInJsonKeysToUnderscores: StrictBool | None = None
    CaseInsensitive: StrictBool | None = None
    ColumnToJsonKeyMappings: dict[StrictStr, StrictStr] | None = None
