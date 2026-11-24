from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxDescribeFileSystemAliasesRequest(BaseModel):
    FileSystemId: StrictStr
    ClientRequestToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
