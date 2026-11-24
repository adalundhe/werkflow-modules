from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_formation_stack_instance_filter import CloudFormationStackInstanceFilter


class CloudFormationListStackInstancesRequest(BaseModel):
    StackSetName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: list[CloudFormationStackInstanceFilter] | None = None
    StackInstanceAccount: StrictStr | None = None
    StackInstanceRegion: StrictStr | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
