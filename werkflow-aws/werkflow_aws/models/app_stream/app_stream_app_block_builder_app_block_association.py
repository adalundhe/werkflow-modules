from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAppBlockBuilderAppBlockAssociation(BaseModel):
    AppBlockArn: StrictStr | None = None
    AppBlockBuilderName: StrictStr | None = None
