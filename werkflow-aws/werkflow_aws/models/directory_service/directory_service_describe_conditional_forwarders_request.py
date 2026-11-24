from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeConditionalForwardersRequest(BaseModel):
    DirectoryId: StrictStr
    RemoteDomainNames: list[StrictStr] | None = None
