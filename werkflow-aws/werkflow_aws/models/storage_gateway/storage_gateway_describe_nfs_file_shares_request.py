from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeNFSFileSharesRequest(BaseModel):
    FileShareARNList: list[StrictStr]
