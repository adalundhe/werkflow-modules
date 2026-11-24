from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .nested_response import NestedResponse


class CreatedIssue(BaseModel):
    id: StrictStr | None = None
    key: StrictStr | None = None
    self: StrictStr | None = None
    transition: NestedResponse | None = None
    watchers: NestedResponse | None = None
