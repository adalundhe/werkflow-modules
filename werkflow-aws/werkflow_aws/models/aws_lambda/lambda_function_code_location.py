from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_function_code_location_error import LambdaFunctionCodeLocationError
from .lambda_resolved_s3_object import LambdaResolvedS3Object


class LambdaFunctionCodeLocation(BaseModel):
    RepositoryType: StrictStr | None = None
    Location: StrictStr | None = None
    ImageUri: StrictStr | None = None
    ResolvedImageUri: StrictStr | None = None
    ResolvedS3Object: LambdaResolvedS3Object | None = None
    SourceKMSKeyArn: StrictStr | None = None
    Error: LambdaFunctionCodeLocationError | None = None
