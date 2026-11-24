from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_connection import AppRunnerConnection


class AppRunnerDeleteConnectionResponse(BaseModel):
    Connection: AppRunnerConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
