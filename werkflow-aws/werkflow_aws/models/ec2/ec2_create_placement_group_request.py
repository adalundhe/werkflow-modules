from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_operator_request import EC2OperatorRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreatePlacementGroupRequest(BaseModel):
    PartitionCount: StrictInt | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    SpreadLevel: Literal['host', 'rack'] | None = None
    LinkedGroupId: StrictStr | None = None
    Operator: EC2OperatorRequest | None = None
    ParentGroupId: StrictStr | None = None
    DryRun: StrictBool | None = None
    GroupName: StrictStr | None = None
    Strategy: Literal['cluster', 'spread', 'partition', 'precision-time'] | None = None
