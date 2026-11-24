from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_status_record import SESStatusRecord


class SESReputationEntity(BaseModel):
    ReputationEntityReference: StrictStr | None = None
    ReputationEntityType: StrictStr | None = None
    ReputationManagementPolicy: StrictStr | None = None
    CustomerManagedStatus: SESStatusRecord | None = None
    AwsSesManagedStatus: SESStatusRecord | None = None
    SendingStatusAggregate: StrictStr | None = None
    ReputationImpact: StrictStr | None = None
