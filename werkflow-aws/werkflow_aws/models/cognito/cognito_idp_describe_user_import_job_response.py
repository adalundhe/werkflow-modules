from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_user_import_job_type import CognitoIDPUserImportJobType


class CognitoIDPDescribeUserImportJobResponse(BaseModel):
    UserImportJob: CognitoIDPUserImportJobType | None = None
    ResponseMetadata: dict[str, Any] | None = None
