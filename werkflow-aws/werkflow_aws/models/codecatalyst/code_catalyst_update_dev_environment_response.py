from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_ide_configuration import CodeCatalystIdeConfiguration


class CodeCatalystUpdateDevEnvironmentResponse(BaseModel):
    id: StrictStr | None = None
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    alias: StrictStr | None = None
    ides: list[CodeCatalystIdeConfiguration] | None = None
    instanceType: StrictStr | None = None
    inactivityTimeoutMinutes: StrictInt | None = None
    clientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
