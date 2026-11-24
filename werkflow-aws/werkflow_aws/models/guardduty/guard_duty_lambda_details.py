from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_tag import GuardDutyTag
from .guard_duty_vpc_config import GuardDutyVpcConfig


class GuardDutyLambdaDetails(BaseModel):
    FunctionArn: StrictStr | None = None
    FunctionName: StrictStr | None = None
    Description: StrictStr | None = None
    LastModifiedAt: datetime.datetime | StrictStr | None = None
    RevisionId: StrictStr | None = None
    FunctionVersion: StrictStr | None = None
    Role: StrictStr | None = None
    VpcConfig: GuardDutyVpcConfig | None = None
    Tags: list[GuardDutyTag] | None = None
