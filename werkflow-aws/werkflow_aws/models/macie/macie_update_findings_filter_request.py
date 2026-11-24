from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_finding_criteria import MacieFindingCriteria


class MacieUpdateFindingsFilterRequest(BaseModel):
    id: StrictStr
    action: Literal['ARCHIVE', 'NOOP'] | None = None
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
    findingCriteria: MacieFindingCriteria | None = None
    name: StrictStr | None = None
    position: StrictInt | None = None
