from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaNamedQueryModel(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Database: StrictStr | None = None
    QueryString: StrictStr | None = None
    NamedQueryId: StrictStr | None = None
    WorkGroup: StrictStr | None = None
