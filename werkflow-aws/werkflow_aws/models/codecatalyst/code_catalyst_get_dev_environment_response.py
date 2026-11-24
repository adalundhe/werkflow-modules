from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_dev_environment_repository_summary import CodeCatalystDevEnvironmentRepositorySummary
from .code_catalyst_ide import CodeCatalystIde
from .code_catalyst_persistent_storage import CodeCatalystPersistentStorage


class CodeCatalystGetDevEnvironmentResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    id: StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    creatorId: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    repositories: list[CodeCatalystDevEnvironmentRepositorySummary] | None = None
    alias: StrictStr | None = None
    ides: list[CodeCatalystIde] | None = None
    instanceType: StrictStr | None = None
    inactivityTimeoutMinutes: StrictInt | None = None
    persistentStorage: CodeCatalystPersistentStorage | None = None
    vpcConnectionName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
