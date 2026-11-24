from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .link_group import LinkGroup


class Operations(BaseModel):
    model_config = ConfigDict(extra="allow")

    linkGroups: list[LinkGroup] | None = None
