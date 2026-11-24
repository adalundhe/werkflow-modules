from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_role_template_version import IAMRoleTemplateVersion


class IAMGetRoleTemplateVersionResponse(BaseModel):
    RoleTemplateVersion: IAMRoleTemplateVersion | None = None
    ResponseMetadata: dict[str, Any] | None = None
