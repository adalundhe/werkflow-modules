from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruEventResource(BaseModel):
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
