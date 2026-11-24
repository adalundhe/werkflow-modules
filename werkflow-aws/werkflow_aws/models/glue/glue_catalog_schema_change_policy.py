from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueCatalogSchemaChangePolicy(BaseModel):
    EnableUpdateCatalog: StrictBool | None = None
    UpdateBehavior: StrictStr | None = None
