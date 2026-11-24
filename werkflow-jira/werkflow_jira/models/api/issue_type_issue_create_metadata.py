from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .field_metadata import FieldMetadata
from .scope import Scope


class IssueTypeIssueCreateMetadata(BaseModel):
    avatarId: StrictInt | None = None
    description: StrictStr | None = None
    entityId: StrictStr | None = None
    expand: StrictStr | None = None
    fields: dict[StrictStr, FieldMetadata] | None = None
    hierarchyLevel: StrictInt | None = None
    iconUrl: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    scope: Scope | None = None
    self: StrictStr | None = None
    subtask: StrictBool | None = None
