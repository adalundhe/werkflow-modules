from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_external_access_details import AccessAnalyzerExternalAccessDetails
from .access_analyzer_internal_access_details import AccessAnalyzerInternalAccessDetails
from .access_analyzer_unused_iam_role_details import AccessAnalyzerUnusedIamRoleDetails
from .access_analyzer_unused_iam_user_access_key_details import AccessAnalyzerUnusedIamUserAccessKeyDetails
from .access_analyzer_unused_iam_user_password_details import AccessAnalyzerUnusedIamUserPasswordDetails
from .access_analyzer_unused_permission_details import AccessAnalyzerUnusedPermissionDetails


class AccessAnalyzerFindingDetails(BaseModel):
    internalAccessDetails: AccessAnalyzerInternalAccessDetails | None = None
    externalAccessDetails: AccessAnalyzerExternalAccessDetails | None = None
    unusedPermissionDetails: AccessAnalyzerUnusedPermissionDetails | None = None
    unusedIamUserAccessKeyDetails: AccessAnalyzerUnusedIamUserAccessKeyDetails | None = None
    unusedIamRoleDetails: AccessAnalyzerUnusedIamRoleDetails | None = None
    unusedIamUserPasswordDetails: AccessAnalyzerUnusedIamUserPasswordDetails | None = None
