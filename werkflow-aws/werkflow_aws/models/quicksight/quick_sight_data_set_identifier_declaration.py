from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSetIdentifierDeclaration(BaseModel):
    Identifier: StrictStr | None = None
    DataSetArn: StrictStr | None = None
