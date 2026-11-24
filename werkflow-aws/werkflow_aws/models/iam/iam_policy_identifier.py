from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .iam_inline_policy_identifier_type import IAMInlinePolicyIdentifierType


class IAMPolicyIdentifier(BaseModel):
    PolicyType: Literal['inline', 'aws-managed', 'user-managed', 'permission-boundary', 'scp', 'rcp'] | None = None
    PolicyArn: StrictStr | None = None
    InlinePolicyIdentifier: IAMInlinePolicyIdentifierType | None = None
