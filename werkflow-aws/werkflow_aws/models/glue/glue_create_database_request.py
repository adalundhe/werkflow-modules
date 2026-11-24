from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_database_input import GlueDatabaseInput


class GlueCreateDatabaseRequest(BaseModel):
    DatabaseInput: GlueDatabaseInput
    CatalogId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
