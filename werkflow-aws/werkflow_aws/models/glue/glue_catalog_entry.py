from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCatalogEntry(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
