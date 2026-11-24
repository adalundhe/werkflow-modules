from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_efs_access_point_posix_user_details import SecurityHubAwsEfsAccessPointPosixUserDetails
from .security_hub_aws_efs_access_point_root_directory_details import SecurityHubAwsEfsAccessPointRootDirectoryDetails


class SecurityHubAwsEfsAccessPointDetails(BaseModel):
    AccessPointId: StrictStr | None = None
    Arn: StrictStr | None = None
    ClientToken: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    PosixUser: SecurityHubAwsEfsAccessPointPosixUserDetails | None = None
    RootDirectory: SecurityHubAwsEfsAccessPointRootDirectoryDetails | None = None
