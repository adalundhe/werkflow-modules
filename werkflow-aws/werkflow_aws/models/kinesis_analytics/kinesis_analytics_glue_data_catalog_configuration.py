from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsGlueDataCatalogConfiguration(BaseModel):
    DatabaseARN: StrictStr
