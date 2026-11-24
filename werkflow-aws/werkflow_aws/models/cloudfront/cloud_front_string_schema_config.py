from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontStringSchemaConfig(BaseModel):
    Comment: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    Required: StrictBool | None = None
