from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_instance_property_filter import SSMInstancePropertyFilter
from .ssm_instance_property_string_filter import SSMInstancePropertyStringFilter


class SSMDescribeInstancePropertiesRequest(BaseModel):
    InstancePropertyFilterList: list[SSMInstancePropertyFilter] | None = None
    FiltersWithOperator: list[SSMInstancePropertyStringFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
