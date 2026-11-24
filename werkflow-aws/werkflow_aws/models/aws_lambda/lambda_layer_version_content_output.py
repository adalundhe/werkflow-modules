from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_resolved_s3_object_model import LambdaResolvedS3ObjectModel


class LambdaLayerVersionContentOutput(BaseModel):
    Location: StrictStr | None = None
    CodeSha256: StrictStr | None = None
    CodeSize: StrictInt | None = None
    SigningProfileVersionArn: StrictStr | None = None
    SigningJobArn: StrictStr | None = None
    ResolvedS3Object: LambdaResolvedS3ObjectModel | None = None
