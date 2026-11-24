from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontConnectionFunctionAssociation(BaseModel):
    Id: StrictStr | None = None
