from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_permissions_boundary_attachment_type import IAMPermissionsBoundaryAttachmentType


class IAMAttachedPermissionsBoundary(BaseModel):
    PermissionsBoundaryType: IAMPermissionsBoundaryAttachmentType | None = None
    PermissionsBoundaryArn: StrictStr | None = None
