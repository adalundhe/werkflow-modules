from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaQueryExecutionContextModel(BaseModel):
    Database: StrictStr | None = None
    Catalog: StrictStr | None = None
