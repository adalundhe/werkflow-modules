from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_replacement_value_entry import IAMReplacementValueEntry


class IAMAcquireRoleRequest(BaseModel):
    TemplateArn: StrictStr
    TemplateMinorVersion: StrictInt | None = None
    ReplacementValues: dict[StrictStr, IAMReplacementValueEntry] | None = None
