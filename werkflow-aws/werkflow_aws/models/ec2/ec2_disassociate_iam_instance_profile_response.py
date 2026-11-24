from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_iam_instance_profile_association import EC2IamInstanceProfileAssociation


class EC2DisassociateIamInstanceProfileResponse(BaseModel):
    IamInstanceProfileAssociation: EC2IamInstanceProfileAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
