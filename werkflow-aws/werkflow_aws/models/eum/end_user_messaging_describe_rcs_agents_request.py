from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_rcs_agent_filter import EndUserMessagingRcsAgentFilter


class EndUserMessagingDescribeRcsAgentsRequest(BaseModel):
    RcsAgentIds: list[StrictStr] | None = None
    Owner: Literal['SELF', 'SHARED'] | None = None
    Filters: list[EndUserMessagingRcsAgentFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
