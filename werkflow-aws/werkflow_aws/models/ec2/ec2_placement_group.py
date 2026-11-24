from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse
from .ec2_tag_model import EC2TagModel


class EC2PlacementGroup(BaseModel):
    GroupName: StrictStr | None = None
    State: StrictStr | None = None
    Strategy: StrictStr | None = None
    PartitionCount: StrictInt | None = None
    GroupId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    GroupArn: StrictStr | None = None
    SpreadLevel: StrictStr | None = None
    LinkedGroupId: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
    ParentGroupId: StrictStr | None = None
