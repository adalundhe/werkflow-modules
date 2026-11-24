from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_application_config import AppStreamApplicationConfig
from .app_stream_runtime_validation_config import AppStreamRuntimeValidationConfig


class AppStreamCreateImportedImageRequest(BaseModel):
    Name: StrictStr
    SourceAmiId: StrictStr | None = None
    WorkspaceImageId: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    RuntimeValidationConfig: AppStreamRuntimeValidationConfig | None = None
    AgentSoftwareVersion: Literal['CURRENT_LATEST', 'ALWAYS_LATEST'] | None = None
    AppCatalogConfig: list[AppStreamApplicationConfig] | None = None
    DryRun: StrictBool | None = None
