from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_assumed_role import MacieAssumedRole
from .macie_aws_account import MacieAwsAccount
from .macie_aws_service import MacieAwsService
from .macie_federated_user import MacieFederatedUser
from .macie_iam_user import MacieIamUser
from .macie_user_identity_root import MacieUserIdentityRoot


class MacieUserIdentity(BaseModel):
    assumedRole: MacieAssumedRole | None = None
    awsAccount: MacieAwsAccount | None = None
    awsService: MacieAwsService | None = None
    federatedUser: MacieFederatedUser | None = None
    iamUser: MacieIamUser | None = None
    root: MacieUserIdentityRoot | None = None
    type: StrictStr | None = None
