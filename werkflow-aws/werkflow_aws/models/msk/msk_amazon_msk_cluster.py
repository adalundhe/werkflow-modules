from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKAmazonMskCluster(BaseModel):
    MskClusterArn: StrictStr | None = None
