from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SimpleLink(BaseModel):
    href: StrictStr | None = None
    iconClass: StrictStr | None = None
    id: StrictStr | None = None
    label: StrictStr | None = None
    styleClass: StrictStr | None = None
    title: StrictStr | None = None
    weight: StrictInt | None = None
