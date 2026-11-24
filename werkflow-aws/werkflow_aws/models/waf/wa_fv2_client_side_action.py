from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_regex import WAFv2Regex


class WAFv2ClientSideAction(BaseModel):
    UsageOfAction: StrictStr | None = None
    Sensitivity: StrictStr | None = None
    ExemptUriRegularExpressions: list[WAFv2Regex] | None = None
