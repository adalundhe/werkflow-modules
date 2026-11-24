from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_parameter_string_filter import SSMParameterStringFilter


class SSMGetParametersByPathRequest(BaseModel):
    Path: StrictStr
    Recursive: StrictBool | None = None
    ParameterFilters: list[SSMParameterStringFilter] | None = None
    WithDecryption: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
