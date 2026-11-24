from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_searchable_contact_attributes_criteria import ConnectSearchableContactAttributesCriteria


class ConnectSearchableContactAttributes(BaseModel):
    Criteria: list[ConnectSearchableContactAttributesCriteria]
    MatchType: Literal['MATCH_ALL', 'MATCH_ANY', 'MATCH_EXACT', 'MATCH_NONE'] | None = None
