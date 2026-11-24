from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectType(BaseModel):
    color: StrictStr | None = None
    descriptionI18nKey: StrictStr | None = None
    formattedKey: StrictStr | None = None
    icon: StrictStr | None = None
    key: StrictStr | None = None
