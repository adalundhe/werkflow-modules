from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCreateIamIdentityCenterConfigOptions(BaseModel):
    instanceArn: StrictStr
    userAttribute: Literal['UserId', 'UserName', 'Email'] | None = None
    groupAttribute: Literal['GroupId', 'GroupName'] | None = None
