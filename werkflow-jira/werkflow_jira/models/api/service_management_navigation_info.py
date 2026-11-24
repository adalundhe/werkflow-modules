from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceManagementNavigationInfo(BaseModel):
    queueCategory: StrictStr | None = None
    queueId: StrictInt | None = None
    queueName: StrictStr | None = None
