from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .scope import Scope


class IssueTypeDetails(BaseModel):
    avatarId: StrictInt | None = None
    description: StrictStr | None = None
    entityId: StrictStr | None = None
    hierarchyLevel: StrictInt | None = None
    iconUrl: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    scope: Scope | None = None
    self: StrictStr | None = None
    subtask: StrictBool | None = None
