from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_severity_level import MacieSeverityLevel


class MacieGetCustomDataIdentifierResponse(BaseModel):
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    deleted: StrictBool | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    ignoreWords: list[StrictStr] | None = None
    keywords: list[StrictStr] | None = None
    maximumMatchDistance: StrictInt | None = None
    name: StrictStr | None = None
    regex: StrictStr | None = None
    severityLevels: list[MacieSeverityLevel] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
