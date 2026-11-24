from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2ResourceTypeOption(BaseModel):
    OptionName: Literal['state-name', 'version-depth'] | None = None
    OptionValues: list[StrictStr] | None = None
