from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectTemplateKey(BaseModel):
    key: StrictStr | None = None
    uuid: StrictStr | None = None
