from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESPutTenantSuppressionAttributesRequest(BaseModel):
    TenantName: StrictStr
    SuppressedReasons: list[Literal['BOUNCE', 'COMPLAINT']] | None = None
    SuppressionScope: Literal['ACCOUNT', 'TENANT'] | None = None
