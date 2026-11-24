from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraPrincipal(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Access: StrictStr | None = None
    DataSourceId: StrictStr | None = None
