from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_iam_policy_constraints import SageMakerIamPolicyConstraints


class SageMakerS3Presign(BaseModel):
    IamPolicyConstraints: SageMakerIamPolicyConstraints | None = None
