from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingPoolFilter(BaseModel):
    Name: Literal['status', 'message-type', 'two-way-enabled', 'self-managed-opt-outs-enabled', 'opt-out-list-name', 'shared-routes-enabled', 'deletion-protection-enabled', 'two-way-channel-arn']
    Values: list[StrictStr]
