from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_iam_instance_profile_specification import EC2IamInstanceProfileSpecification


class EC2ReplaceIamInstanceProfileAssociationRequest(BaseModel):
    IamInstanceProfile: EC2IamInstanceProfileSpecification
    AssociationId: StrictStr
