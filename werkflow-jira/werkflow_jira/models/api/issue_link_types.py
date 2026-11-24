from __future__ import annotations
from pydantic import BaseModel
from .issue_link_type import IssueLinkType


class IssueLinkTypes(BaseModel):
    issueLinkTypes: list[IssueLinkType] | None = None
