from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePutWorkflowRunPropertiesRequest(BaseModel):
    Name: StrictStr
    RunId: StrictStr
    RunProperties: dict[StrictStr, StrictStr]
