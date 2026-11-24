from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueMicrosoftSQLServerCatalogTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
