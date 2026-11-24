from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_database_input import GlueDatabaseInput


class GlueUpdateDatabaseRequest(BaseModel):
    Name: StrictStr
    DatabaseInput: GlueDatabaseInput
    CatalogId: StrictStr | None = None
