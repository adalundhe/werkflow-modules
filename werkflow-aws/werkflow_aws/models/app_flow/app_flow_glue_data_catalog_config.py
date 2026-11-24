from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowGlueDataCatalogConfig(BaseModel):
    roleArn: StrictStr | None = None
    databaseName: StrictStr | None = None
    tablePrefix: StrictStr | None = None
