from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_describe_activations_filter import SSMDescribeActivationsFilter


class SSMDescribeActivationsRequest(BaseModel):
    Filters: list[SSMDescribeActivationsFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
