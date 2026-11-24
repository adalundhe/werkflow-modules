from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_video_list_edge_agent_configurations_edge_config import KinesisVideoListEdgeAgentConfigurationsEdgeConfig


class KinesisVideoListEdgeAgentConfigurationsResponse(BaseModel):
    EdgeConfigs: list[KinesisVideoListEdgeAgentConfigurationsEdgeConfig] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
