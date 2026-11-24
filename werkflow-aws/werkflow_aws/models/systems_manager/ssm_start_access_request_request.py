from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_tag import SSMTag
from .ssm_target import SSMTarget


class SSMStartAccessRequestRequest(BaseModel):
    Reason: StrictStr
    Targets: list[SSMTarget]
    Tags: list[SSMTag] | None = None
