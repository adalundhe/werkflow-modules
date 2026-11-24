from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_finding_criteria import MacieFindingCriteria


class MacieGetFindingsFilterResponse(BaseModel):
    action: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    findingCriteria: MacieFindingCriteria | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    position: StrictInt | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
