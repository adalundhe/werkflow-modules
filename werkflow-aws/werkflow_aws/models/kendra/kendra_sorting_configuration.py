from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KendraSortingConfiguration(BaseModel):
    DocumentAttributeKey: StrictStr
    SortOrder: Literal['DESC', 'ASC']
