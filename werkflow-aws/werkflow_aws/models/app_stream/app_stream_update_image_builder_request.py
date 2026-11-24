from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_image_builder_agent_access_config_for_update import AppStreamImageBuilderAgentAccessConfigForUpdate


class AppStreamUpdateImageBuilderRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    AgentAccessConfig: AppStreamImageBuilderAgentAccessConfigForUpdate | None = None
    AttributesToDelete: list[Literal['AGENT_ACCESS_CONFIG']] | None = None
