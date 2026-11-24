from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class WAFv2SettlementRecord(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    PayerAddress: StrictStr | None = None
    WalletAddress: StrictStr | None = None
    Status: StrictStr | None = None
    Amount: StrictStr | None = None
    Currency: StrictStr | None = None
    Network: StrictStr | None = None
    TransactionId: StrictStr | None = None
    RequestId: StrictStr | None = None
    SourceName: StrictStr | None = None
    Organization: StrictStr | None = None
    SourceCategory: StrictStr | None = None
    Intent: StrictStr | None = None
    Verified: StrictBool | None = None
    ContentPath: StrictStr | None = None
    WebAclArn: StrictStr | None = None
    RequestTimestamp: datetime.datetime | StrictStr | None = None
