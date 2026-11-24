from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2AddressTransfer(BaseModel):
    PublicIp: StrictStr | None = None
    AllocationId: StrictStr | None = None
    TransferAccountId: StrictStr | None = None
    TransferOfferExpirationTimestamp: datetime.datetime | StrictStr | None = None
    TransferOfferAcceptedTimestamp: datetime.datetime | StrictStr | None = None
    AddressTransferStatus: StrictStr | None = None
