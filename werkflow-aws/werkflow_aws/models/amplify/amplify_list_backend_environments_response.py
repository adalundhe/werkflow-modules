from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_backend_environment import AmplifyBackendEnvironment


class AmplifyListBackendEnvironmentsResponse(BaseModel):
    backendEnvironments: list[AmplifyBackendEnvironment] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
