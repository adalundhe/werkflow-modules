from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_backend_environment import AmplifyBackendEnvironment


class AmplifyGetBackendEnvironmentResponse(BaseModel):
    backendEnvironment: AmplifyBackendEnvironment | None = None
    ResponseMetadata: dict[str, Any] | None = None
