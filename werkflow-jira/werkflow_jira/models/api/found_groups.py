from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .found_group import FoundGroup


class FoundGroups(BaseModel):
    groups: list[FoundGroup] | None = None
    header: StrictStr | None = None
    total: StrictInt | None = None
