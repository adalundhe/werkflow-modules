from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EndUserMessagingOptOutListInformation(BaseModel):
    OptOutListArn: StrictStr | None = None
    OptOutListName: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
