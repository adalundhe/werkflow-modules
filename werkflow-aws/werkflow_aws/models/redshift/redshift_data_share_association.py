from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftDataShareAssociation(BaseModel):
    ConsumerIdentifier: StrictStr | None = None
    Status: StrictStr | None = None
    ConsumerRegion: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    StatusChangeDate: datetime.datetime | StrictStr | None = None
    ProducerAllowedWrites: StrictBool | None = None
    ConsumerAcceptedWrites: StrictBool | None = None
