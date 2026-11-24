from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListControlsRequest(BaseModel):
    controlType: Literal['Standard', 'Custom', 'Core']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    controlCatalogId: StrictStr | None = None
