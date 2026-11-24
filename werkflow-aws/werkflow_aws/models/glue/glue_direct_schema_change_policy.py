from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDirectSchemaChangePolicy(BaseModel):
    EnableUpdateCatalog: StrictBool | None = None
    UpdateBehavior: StrictStr | None = None
    Table: StrictStr | None = None
    Database: StrictStr | None = None
