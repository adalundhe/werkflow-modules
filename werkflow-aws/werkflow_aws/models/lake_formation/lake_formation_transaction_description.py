from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LakeFormationTransactionDescription(BaseModel):
    TransactionId: StrictStr | None = None
    TransactionStatus: StrictStr | None = None
    TransactionStartTime: datetime.datetime | StrictStr | None = None
    TransactionEndTime: datetime.datetime | StrictStr | None = None
