from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectNameCriteria(BaseModel):
    SearchText: list[StrictStr]
    MatchType: Literal['MATCH_ALL', 'MATCH_ANY', 'MATCH_EXACT', 'MATCH_NONE']
