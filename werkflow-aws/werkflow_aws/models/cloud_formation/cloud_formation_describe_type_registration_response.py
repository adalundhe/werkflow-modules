from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeTypeRegistrationResponse(BaseModel):
    ProgressStatus: StrictStr | None = None
    Description: StrictStr | None = None
    TypeArn: StrictStr | None = None
    TypeVersionArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
