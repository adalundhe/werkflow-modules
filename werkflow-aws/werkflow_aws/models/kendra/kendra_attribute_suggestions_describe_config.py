from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_suggestable_config import KendraSuggestableConfig


class KendraAttributeSuggestionsDescribeConfig(BaseModel):
    SuggestableConfigList: list[KendraSuggestableConfig] | None = None
    AttributeSuggestionsMode: StrictStr | None = None
