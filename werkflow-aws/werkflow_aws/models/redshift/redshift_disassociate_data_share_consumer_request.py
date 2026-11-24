from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftDisassociateDataShareConsumerRequest(BaseModel):
    DataShareArn: StrictStr
    DisassociateEntireAccount: StrictBool | None = None
    ConsumerArn: StrictStr | None = None
    ConsumerRegion: StrictStr | None = None
