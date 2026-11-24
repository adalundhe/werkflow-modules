from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_session import SSMSession


class SSMDescribeSessionsResponse(BaseModel):
    Sessions: list[SSMSession] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
