from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetSchemaCreationStatusRequest(BaseModel):
    apiId: StrictStr
