from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_import_job_type import CognitoIDPUserImportJobType


class CognitoIDPListUserImportJobsResponse(BaseModel):
    UserImportJobs: list[CognitoIDPUserImportJobType] | None = None
    PaginationToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
