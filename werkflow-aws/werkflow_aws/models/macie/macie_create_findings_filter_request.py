from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_finding_criteria import MacieFindingCriteria


class MacieCreateFindingsFilterRequest(BaseModel):
    action: Literal['ARCHIVE', 'NOOP']
    findingCriteria: MacieFindingCriteria
    name: StrictStr
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
    position: StrictInt | None = None
    tags: dict[StrictStr, StrictStr] | None = None
