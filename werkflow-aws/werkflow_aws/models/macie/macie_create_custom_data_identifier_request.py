from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_severity_level import MacieSeverityLevel


class MacieCreateCustomDataIdentifierRequest(BaseModel):
    name: StrictStr
    regex: StrictStr
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
    ignoreWords: list[StrictStr] | None = None
    keywords: list[StrictStr] | None = None
    maximumMatchDistance: StrictInt | None = None
    severityLevels: list[MacieSeverityLevel] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
