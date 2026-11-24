from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_parameter_inline_policy import SSMParameterInlinePolicy


class SSMParameterHistory(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    KeyId: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    LastModifiedUser: StrictStr | None = None
    Description: StrictStr | None = None
    Value: StrictStr | None = None
    AllowedPattern: StrictStr | None = None
    Version: StrictInt | None = None
    Labels: list[StrictStr] | None = None
    Tier: StrictStr | None = None
    Policies: list[SSMParameterInlinePolicy] | None = None
    DataType: StrictStr | None = None
