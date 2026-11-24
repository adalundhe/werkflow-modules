from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexKendraConfiguration(BaseModel):
    kendraIndex: StrictStr | None = None
    queryFilterStringEnabled: StrictBool | None = None
    queryFilterString: StrictStr | None = None
