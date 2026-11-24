from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDateTimeConverter(BaseModel):
    source: StrictStr | None = None
    target: StrictStr | None = None
    targetFormat: StrictStr | None = None
    matchPatterns: list[StrictStr] | None = None
    sourceTimezone: StrictStr | None = None
    targetTimezone: StrictStr | None = None
    locale: StrictStr | None = None
