from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontLambdaFunctionAssociation(BaseModel):
    LambdaFunctionARN: StrictStr | None = None
    EventType: StrictStr | None = None
    IncludeBody: StrictBool | None = None
