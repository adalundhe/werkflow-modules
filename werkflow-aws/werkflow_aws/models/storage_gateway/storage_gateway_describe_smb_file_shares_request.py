from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeSMBFileSharesRequest(BaseModel):
    FileShareARNList: list[StrictStr]
