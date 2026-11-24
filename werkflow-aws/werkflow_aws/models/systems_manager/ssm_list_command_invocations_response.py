from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_command_invocation import SSMCommandInvocation


class SSMListCommandInvocationsResponse(BaseModel):
    CommandInvocations: list[SSMCommandInvocation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
