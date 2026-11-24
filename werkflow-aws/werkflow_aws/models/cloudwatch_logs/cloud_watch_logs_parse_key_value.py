from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsParseKeyValue(BaseModel):
    source: StrictStr | None = None
    destination: StrictStr | None = None
    fieldDelimiter: StrictStr | None = None
    keyValueDelimiter: StrictStr | None = None
    keyPrefix: StrictStr | None = None
    nonMatchValue: StrictStr | None = None
    overwriteIfExists: StrictBool | None = None
