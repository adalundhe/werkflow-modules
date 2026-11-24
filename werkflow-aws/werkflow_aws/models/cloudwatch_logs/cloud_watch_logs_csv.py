from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsCSV(BaseModel):
    quoteCharacter: StrictStr | None = None
    delimiter: StrictStr | None = None
    columns: list[StrictStr] | None = None
    source: StrictStr | None = None
    destination: StrictStr | None = None
