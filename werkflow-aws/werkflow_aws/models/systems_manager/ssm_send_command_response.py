from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_command import SSMCommand


class SSMSendCommandResponse(BaseModel):
    Command: SSMCommand | None = None
    ResponseMetadata: dict[str, Any] | None = None
