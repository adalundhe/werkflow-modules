from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_tag import GuardDutyTag


class GuardDutyEksClusterDetails(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    VpcId: StrictStr | None = None
    Status: StrictStr | None = None
    Tags: list[GuardDutyTag] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
