from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_artifact_package_group_origin_configuration import CodeArtifactPackageGroupOriginConfiguration
from .code_artifact_package_group_reference import CodeArtifactPackageGroupReference


class CodeArtifactPackageGroupDescription(BaseModel):
    arn: StrictStr | None = None
    pattern: StrictStr | None = None
    domainName: StrictStr | None = None
    domainOwner: StrictStr | None = None
    createdTime: datetime.datetime | StrictStr | None = None
    contactInfo: StrictStr | None = None
    description: StrictStr | None = None
    originConfiguration: CodeArtifactPackageGroupOriginConfiguration | None = None
    parent: CodeArtifactPackageGroupReference | None = None
