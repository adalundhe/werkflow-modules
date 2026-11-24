from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyLambdaFunction(BaseModel):
    FunctionName: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    FunctionVersion: StrictStr | None = None
    Role: StrictStr | None = None
    Description: StrictStr | None = None
    RevisionId: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    VpcConfigurationSummary: StrictStr | None = None
