from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SSMDescribeDocumentPermissionRequest(BaseModel):
    Name: StrictStr
    PermissionType: Literal['Share']
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
