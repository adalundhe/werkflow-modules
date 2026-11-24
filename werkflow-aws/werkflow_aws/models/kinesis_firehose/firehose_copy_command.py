from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseCopyCommand(BaseModel):
    DataTableName: StrictStr | None = None
    DataTableColumns: StrictStr | None = None
    CopyOptions: StrictStr | None = None
