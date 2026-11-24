from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_dev_environment_access_details import CodeCatalystDevEnvironmentAccessDetails


class CodeCatalystStartDevEnvironmentSessionResponse(BaseModel):
    accessDetails: CodeCatalystDevEnvironmentAccessDetails | None = None
    sessionId: StrictStr | None = None
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    id: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
