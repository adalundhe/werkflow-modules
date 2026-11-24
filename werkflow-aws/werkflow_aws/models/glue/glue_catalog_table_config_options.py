from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCatalogTableConfigOptions(BaseModel):
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    S3Location: StrictStr | None = None
    CatalogId: StrictStr | None = None
