from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsGlueDataCatalogConfigurationUpdate(BaseModel):
    DatabaseARNUpdate: StrictStr
