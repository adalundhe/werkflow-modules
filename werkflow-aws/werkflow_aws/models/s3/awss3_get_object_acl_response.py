from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel
from .awss3_grant import AWSS3Grant
from .awss3_owner import AWSS3Owner


class AWSS3GetObjectAclResponse(BaseModel):
    Owner: AWSS3Owner | None = None
    Grants: list[AWSS3Grant] | None = None
    RequestCharged: Literal['requester'] | None = None
    ResponseMetadata: dict[str, Any] | None = None
