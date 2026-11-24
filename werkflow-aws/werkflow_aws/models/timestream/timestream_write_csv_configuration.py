from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TimestreamWriteCsvConfiguration(BaseModel):
    ColumnSeparator: StrictStr | None = None
    EscapeChar: StrictStr | None = None
    QuoteChar: StrictStr | None = None
    NullValue: StrictStr | None = None
    TrimWhiteSpace: StrictBool | None = None
