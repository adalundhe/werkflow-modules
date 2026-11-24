from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .kendra_suggestable_config import KendraSuggestableConfig


class KendraAttributeSuggestionsUpdateConfig(BaseModel):
    SuggestableConfigList: list[KendraSuggestableConfig] | None = None
    AttributeSuggestionsMode: Literal['ACTIVE', 'INACTIVE'] | None = None
