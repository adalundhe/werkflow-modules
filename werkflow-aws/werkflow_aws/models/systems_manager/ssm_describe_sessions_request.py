from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_session_filter import SSMSessionFilter


class SSMDescribeSessionsRequest(BaseModel):
    State: Literal['Active', 'History']
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[SSMSessionFilter] | None = None
