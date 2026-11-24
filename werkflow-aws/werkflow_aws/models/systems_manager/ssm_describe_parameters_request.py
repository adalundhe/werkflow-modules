from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_parameter_string_filter import SSMParameterStringFilter
from .ssm_parameters_filter import SSMParametersFilter


class SSMDescribeParametersRequest(BaseModel):
    Filters: list[SSMParametersFilter] | None = None
    ParameterFilters: list[SSMParameterStringFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Shared: StrictBool | None = None
