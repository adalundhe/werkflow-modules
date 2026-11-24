from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsAgentFilter(BaseModel):
    Name: Literal['status', 'two-way-enabled', 'self-managed-opt-outs-enabled', 'opt-out-list-name', 'deletion-protection-enabled', 'two-way-channel-arn']
    Values: list[StrictStr]
