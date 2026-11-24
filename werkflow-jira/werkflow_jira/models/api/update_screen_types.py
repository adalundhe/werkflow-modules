from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UpdateScreenTypes(BaseModel):
    create: StrictStr | None = None
    default: StrictStr | None = None
    edit: StrictStr | None = None
    view: StrictStr | None = None
