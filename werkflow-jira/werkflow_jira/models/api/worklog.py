from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from .entity_property import EntityProperty
from .user_details import UserDetails
from .visibility import Visibility


class Worklog(BaseModel):
    model_config = ConfigDict(extra="allow")

    author: UserDetails | None = None
    comment: Any = None
    created: StrictStr | None = None
    id: StrictStr | None = None
    issueId: StrictStr | None = None
    properties: list[EntityProperty] | None = None
    self: StrictStr | None = None
    started: StrictStr | None = None
    timeSpent: StrictStr | None = None
    timeSpentSeconds: StrictInt | None = None
    updateAuthor: UserDetails | None = None
    updated: StrictStr | None = None
    visibility: Visibility | None = None
