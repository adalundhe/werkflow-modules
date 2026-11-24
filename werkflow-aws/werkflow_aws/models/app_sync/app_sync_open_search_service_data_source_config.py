from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncOpenSearchServiceDataSourceConfig(BaseModel):
    endpoint: StrictStr | None = None
    awsRegion: StrictStr | None = None
