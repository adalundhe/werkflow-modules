from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSnowflakeConnectorProfileProperties(BaseModel):
    warehouse: StrictStr | None = None
    stage: StrictStr | None = None
    bucketName: StrictStr | None = None
    bucketPrefix: StrictStr | None = None
    privateLinkServiceName: StrictStr | None = None
    accountName: StrictStr | None = None
    region: StrictStr | None = None
