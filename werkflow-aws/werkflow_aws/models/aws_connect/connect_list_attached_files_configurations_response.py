from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_attached_files_configuration_summary import ConnectAttachedFilesConfigurationSummary


class ConnectListAttachedFilesConfigurationsResponse(BaseModel):
    AttachedFilesConfigurations: list[ConnectAttachedFilesConfigurationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
