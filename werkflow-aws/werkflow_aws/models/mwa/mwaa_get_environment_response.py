from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .mwaa_environment import MWAAEnvironment


class MWAAGetEnvironmentResponse(BaseModel):
    Environment: MWAAEnvironment | None = None
    ResponseMetadata: dict[str, Any] | None = None
