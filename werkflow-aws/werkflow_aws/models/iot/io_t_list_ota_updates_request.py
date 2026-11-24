from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListOTAUpdatesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    otaUpdateStatus: Literal['CREATE_PENDING', 'CREATE_IN_PROGRESS', 'CREATE_COMPLETE', 'CREATE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_FAILED'] | None = None
