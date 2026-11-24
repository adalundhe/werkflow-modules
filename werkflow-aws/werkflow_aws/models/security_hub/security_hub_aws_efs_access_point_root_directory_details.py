from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_efs_access_point_root_directory_creation_info_details import SecurityHubAwsEfsAccessPointRootDirectoryCreationInfoDetails


class SecurityHubAwsEfsAccessPointRootDirectoryDetails(BaseModel):
    CreationInfo: SecurityHubAwsEfsAccessPointRootDirectoryCreationInfoDetails | None = None
    Path: StrictStr | None = None
