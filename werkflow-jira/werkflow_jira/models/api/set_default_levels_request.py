from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .default_level_value import DefaultLevelValue


class SetDefaultLevelsRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    defaultValues: list[DefaultLevelValue] | None = None
