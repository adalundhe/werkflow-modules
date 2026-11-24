from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedBlockchainApprovalThresholdPolicy(BaseModel):
    ThresholdPercentage: StrictInt | None = None
    ProposalDurationInHours: StrictInt | None = None
    ThresholdComparator: StrictStr | None = None
