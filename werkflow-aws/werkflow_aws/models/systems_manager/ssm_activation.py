from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_tag import SSMTag


class SSMActivation(BaseModel):
    ActivationId: StrictStr | None = None
    Description: StrictStr | None = None
    DefaultInstanceName: StrictStr | None = None
    IamRole: StrictStr | None = None
    RegistrationLimit: StrictInt | None = None
    RegistrationsCount: StrictInt | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    Expired: StrictBool | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    Tags: list[SSMTag] | None = None
