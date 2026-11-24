from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaLayer(BaseModel):
    Arn: StrictStr | None = None
    CodeSize: StrictInt | None = None
    SigningProfileVersionArn: StrictStr | None = None
    SigningJobArn: StrictStr | None = None
