from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_approval_threshold_policy import ManagedBlockchainApprovalThresholdPolicy


class ManagedBlockchainVotingPolicy(BaseModel):
    ApprovalThresholdPolicy: ManagedBlockchainApprovalThresholdPolicy | None = None
