from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_formation_type_filters import CloudFormationTypeFilters


class CloudFormationListTypesRequest(BaseModel):
    Visibility: Literal['PUBLIC', 'PRIVATE'] | None = None
    ProvisioningType: Literal['NON_PROVISIONABLE', 'IMMUTABLE', 'FULLY_MUTABLE'] | None = None
    DeprecatedStatus: Literal['LIVE', 'DEPRECATED'] | None = None
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    Filters: CloudFormationTypeFilters | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
