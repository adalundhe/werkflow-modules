from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .support_category import SupportCategory


class SupportService(BaseModel):
    code: StrictStr | None = None
    name: StrictStr | None = None
    categories: list[SupportCategory] | None = None
