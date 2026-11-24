from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_acl_grantee import AccessAnalyzerAclGrantee


class AccessAnalyzerS3BucketAclGrantConfiguration(BaseModel):
    permission: StrictStr | None = None
    grantee: AccessAnalyzerAclGrantee | None = None
