from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_rcs_agent_information import EndUserMessagingRcsAgentInformation


class EndUserMessagingDescribeRcsAgentsResponse(BaseModel):
    RcsAgents: list[EndUserMessagingRcsAgentInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
