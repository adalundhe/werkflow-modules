from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_tag import AppRunnerTag


class AppRunnerListTagsForResourceResponse(BaseModel):
    Tags: list[AppRunnerTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
