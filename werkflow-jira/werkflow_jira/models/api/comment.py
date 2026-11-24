from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from .entity_property import EntityProperty
from .user_details import UserDetails
from .visibility import Visibility


class Comment(BaseModel):
    model_config = ConfigDict(extra="allow")

    author: UserDetails | None = None
    body: Any = None
    created: StrictStr | None = None
    id: StrictStr | None = None
    jsdAuthorCanSeeRequest: StrictBool | None = None
    jsdPublic: StrictBool | None = None
    properties: list[EntityProperty] | None = None
    renderedBody: StrictStr | None = None
    self: StrictStr | None = None
    updateAuthor: UserDetails | None = None
    updated: StrictStr | None = None
    visibility: Visibility | None = None
