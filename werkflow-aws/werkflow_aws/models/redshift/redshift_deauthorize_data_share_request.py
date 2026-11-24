from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeauthorizeDataShareRequest(BaseModel):
    DataShareArn: StrictStr
    ConsumerIdentifier: StrictStr
