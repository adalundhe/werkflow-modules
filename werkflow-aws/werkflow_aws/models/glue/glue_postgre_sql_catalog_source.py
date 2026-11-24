from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePostgreSQLCatalogSource(BaseModel):
    Name: StrictStr | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
