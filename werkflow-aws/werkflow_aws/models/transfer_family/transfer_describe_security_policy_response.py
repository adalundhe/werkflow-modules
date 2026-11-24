from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_security_policy import TransferDescribedSecurityPolicy


class TransferDescribeSecurityPolicyResponse(BaseModel):
    SecurityPolicy: TransferDescribedSecurityPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
