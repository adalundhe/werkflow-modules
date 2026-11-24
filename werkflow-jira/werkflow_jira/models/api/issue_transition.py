from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from .field_metadata import FieldMetadata
from .status_details import StatusDetails


class IssueTransition(BaseModel):
    model_config = ConfigDict(extra="allow")

    expand: StrictStr | None = None
    fields: dict[StrictStr, FieldMetadata] | None = None
    hasScreen: StrictBool | None = None
    id: StrictStr | None = None
    isAvailable: StrictBool | None = None
    isConditional: StrictBool | None = None
    isGlobal: StrictBool | None = None
    isInitial: StrictBool | None = None
    looped: StrictBool | None = None
    name: StrictStr | None = None
    to: StatusDetails | None = None
