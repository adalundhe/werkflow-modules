from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .simple_link import SimpleLink


class LinkGroup(BaseModel):
    groups: list[LinkGroup] | None = None
    header: SimpleLink | None = None
    id: StrictStr | None = None
    links: list[SimpleLink] | None = None
    styleClass: StrictStr | None = None
    weight: StrictInt | None = None
