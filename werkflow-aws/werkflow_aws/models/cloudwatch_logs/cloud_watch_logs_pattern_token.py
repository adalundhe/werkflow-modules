from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsPatternToken(BaseModel):
    dynamicTokenPosition: StrictInt | None = None
    isDynamic: StrictBool | None = None
    tokenString: StrictStr | None = None
    enumerations: dict[StrictStr, StrictInt] | None = None
    inferredTokenName: StrictStr | None = None
