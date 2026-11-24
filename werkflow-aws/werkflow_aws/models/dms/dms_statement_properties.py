from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSStatementProperties(BaseModel):
    Definition: StrictStr
