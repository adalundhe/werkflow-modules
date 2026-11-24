from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_instance_information import SSMInstanceInformation


class SSMDescribeInstanceInformationResponse(BaseModel):
    InstanceInformationList: list[SSMInstanceInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
