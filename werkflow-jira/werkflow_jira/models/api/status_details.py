from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .scope import Scope
from .status_category import StatusCategory


class StatusDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    iconUrl: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    scope: Scope | None = None
    self: StrictStr | None = None
    statusCategory: StatusCategory | None = None
