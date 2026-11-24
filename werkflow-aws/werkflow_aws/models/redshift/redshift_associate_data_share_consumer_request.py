from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftAssociateDataShareConsumerRequest(BaseModel):
    DataShareArn: StrictStr
    AssociateEntireAccount: StrictBool | None = None
    ConsumerArn: StrictStr | None = None
    ConsumerRegion: StrictStr | None = None
    AllowWrites: StrictBool | None = None
