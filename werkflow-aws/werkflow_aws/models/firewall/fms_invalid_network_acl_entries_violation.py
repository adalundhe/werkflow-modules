from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_entry_violation import FMSEntryViolation


class FMSInvalidNetworkAclEntriesViolation(BaseModel):
    Vpc: StrictStr | None = None
    Subnet: StrictStr | None = None
    SubnetAvailabilityZone: StrictStr | None = None
    CurrentAssociatedNetworkAcl: StrictStr | None = None
    EntryViolations: list[FMSEntryViolation] | None = None
