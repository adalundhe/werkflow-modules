from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_tag import AppRunnerTag


class AppRunnerTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[AppRunnerTag]
