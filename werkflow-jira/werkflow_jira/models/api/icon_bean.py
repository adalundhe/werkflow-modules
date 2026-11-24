from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IconBean(BaseModel):
    link: StrictStr | None = None
    title: StrictStr | None = None
    url16x16: StrictStr | None = None
