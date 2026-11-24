from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneCreateNotebookRequest(BaseModel):
    domainIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    name: StrictStr
    description: StrictStr | None = None
    type: Literal['DATA', 'SQL'] | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    clientToken: StrictStr | None = None
