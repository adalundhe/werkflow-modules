from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_agent_list_entry import DataSyncAgentListEntry


class DataSyncListAgentsResponse(BaseModel):
    Agents: list[DataSyncAgentListEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
