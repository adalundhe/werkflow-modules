from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_command import SSMCommand


class SSMListCommandsResponse(BaseModel):
    Commands: list[SSMCommand] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
