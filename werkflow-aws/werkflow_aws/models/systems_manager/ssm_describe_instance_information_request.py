from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_instance_information_filter import SSMInstanceInformationFilter
from .ssm_instance_information_string_filter import SSMInstanceInformationStringFilter


class SSMDescribeInstanceInformationRequest(BaseModel):
    InstanceInformationFilterList: list[SSMInstanceInformationFilter] | None = None
    Filters: list[SSMInstanceInformationStringFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
