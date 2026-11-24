from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_email_address import CodeCatalystEmailAddress


class CodeCatalystGetUserDetailsResponse(BaseModel):
    userId: StrictStr | None = None
    userName: StrictStr | None = None
    displayName: StrictStr | None = None
    primaryEmail: CodeCatalystEmailAddress | None = None
    version: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
