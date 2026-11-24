from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class MultipleCustomFieldValuesUpdate(BaseModel):
    customField: StrictStr | None = None
    issueIds: list[StrictInt] | None = None
    value: Any = None
