from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDataCatalogConfig(BaseModel):
    TableName: StrictStr | None = None
    Catalog: StrictStr | None = None
    Database: StrictStr | None = None
