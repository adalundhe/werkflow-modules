from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_iam_instance_profile_association import EC2IamInstanceProfileAssociation


class EC2DescribeIamInstanceProfileAssociationsResponse(BaseModel):
    IamInstanceProfileAssociations: list[EC2IamInstanceProfileAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
