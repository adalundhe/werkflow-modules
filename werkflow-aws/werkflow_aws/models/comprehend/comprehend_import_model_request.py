from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_tag import ComprehendTag


class ComprehendImportModelRequest(BaseModel):
    SourceModelArn: StrictStr
    ModelName: StrictStr | None = None
    VersionName: StrictStr | None = None
    ModelKmsKeyId: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
