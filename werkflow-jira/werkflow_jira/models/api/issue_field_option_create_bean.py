from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictStr
from .issue_field_option_configuration import IssueFieldOptionConfiguration


class IssueFieldOptionCreateBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    config: IssueFieldOptionConfiguration | None = None
    properties: dict[StrictStr, Any] | None = None
    value: StrictStr | None = None
