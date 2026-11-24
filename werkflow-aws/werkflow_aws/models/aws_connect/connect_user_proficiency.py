from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectUserProficiency(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeValue: StrictStr | None = None
    Level: StrictFloat | StrictInt | None = None
