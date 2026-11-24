from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSTableToReload(BaseModel):
    SchemaName: StrictStr
    TableName: StrictStr
