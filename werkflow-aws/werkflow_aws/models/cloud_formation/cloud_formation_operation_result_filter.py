from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationOperationResultFilter(BaseModel):
    Name: Literal['OPERATION_RESULT_STATUS'] | None = None
    Values: StrictStr | None = None
