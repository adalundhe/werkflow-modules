from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_backend_environment import AmplifyBackendEnvironment


class AmplifyDeleteBackendEnvironmentResponse(BaseModel):
    backendEnvironment: AmplifyBackendEnvironment | None = None
    ResponseMetadata: dict[str, Any] | None = None
