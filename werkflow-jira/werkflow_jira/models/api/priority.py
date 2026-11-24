from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from .expand_priority_scheme_page import ExpandPrioritySchemePage


class Priority(BaseModel):
    model_config = ConfigDict(extra="allow")

    avatarId: StrictInt | None = None
    description: StrictStr | None = None
    iconUrl: StrictStr | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    name: StrictStr | None = None
    schemes: ExpandPrioritySchemePage | None = None
    self: StrictStr | None = None
    statusColor: StrictStr | None = None
