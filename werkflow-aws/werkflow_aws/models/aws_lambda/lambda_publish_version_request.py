from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_function_version_latest_published import LambdaFunctionVersionLatestPublished


class LambdaPublishVersionRequest(BaseModel):
    FunctionName: StrictStr
    CodeSha256: StrictStr | None = None
    Description: StrictStr | None = None
    RevisionId: StrictStr | None = None
    PublishTo: LambdaFunctionVersionLatestPublished | None = None
