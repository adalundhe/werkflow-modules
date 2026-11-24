from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ScheduledInstancesIamInstanceProfile(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
