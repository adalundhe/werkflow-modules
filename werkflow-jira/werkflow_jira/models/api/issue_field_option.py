from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .issue_field_option_configuration import IssueFieldOptionConfiguration


class IssueFieldOption(BaseModel):
    config: IssueFieldOptionConfiguration | None = None
    id: StrictInt | None = None
    properties: dict[StrictStr, Any] | None = None
    value: StrictStr | None = None
