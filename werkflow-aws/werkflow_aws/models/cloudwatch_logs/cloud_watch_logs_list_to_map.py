from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsListToMap(BaseModel):
    source: StrictStr | None = None
    key: StrictStr | None = None
    valueKey: StrictStr | None = None
    target: StrictStr | None = None
    flatten: StrictBool | None = None
    flattenedElement: StrictStr | None = None
