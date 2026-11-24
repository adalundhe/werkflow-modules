from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreDescribeContainerRequest(BaseModel):
    ContainerName: StrictStr | None = None
