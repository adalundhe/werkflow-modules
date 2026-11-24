from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCloudWatchDirectQueryDataSource(BaseModel):
    RoleArn: StrictStr | None = None
