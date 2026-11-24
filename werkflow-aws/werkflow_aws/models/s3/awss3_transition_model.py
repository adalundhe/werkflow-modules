from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3TransitionModel(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    Days: StrictInt | None = None
    StorageClass: StrictStr | None = None
