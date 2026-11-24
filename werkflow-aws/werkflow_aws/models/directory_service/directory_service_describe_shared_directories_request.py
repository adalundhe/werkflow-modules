from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceDescribeSharedDirectoriesRequest(BaseModel):
    OwnerDirectoryId: StrictStr
    SharedDirectoryIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
