from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMDescribeActivationsFilter(BaseModel):
    FilterKey: Literal['ActivationIds', 'DefaultInstanceName', 'IamRole'] | None = None
    FilterValues: list[StrictStr] | None = None
