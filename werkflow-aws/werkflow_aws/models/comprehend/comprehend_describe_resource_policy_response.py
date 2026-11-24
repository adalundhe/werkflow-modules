from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendDescribeResourcePolicyResponse(BaseModel):
    ResourcePolicy: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    PolicyRevisionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
