from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class OpenSearchServerlessUpdateIamIdentityCenterConfigOptions(BaseModel):
    userAttribute: Literal['UserId', 'UserName', 'Email'] | None = None
    groupAttribute: Literal['GroupId', 'GroupName'] | None = None
