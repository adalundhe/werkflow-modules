from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_specification import EC2InstanceSpecification
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateSnapshotsRequest(BaseModel):
    InstanceSpecification: EC2InstanceSpecification
    Description: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    CopyTagsFromSource: Literal['volume'] | None = None
    Location: Literal['regional', 'local'] | None = None
