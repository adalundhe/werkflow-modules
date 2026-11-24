from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsGlueDataCatalogConfigurationDescription(BaseModel):
    DatabaseARN: StrictStr | None = None
