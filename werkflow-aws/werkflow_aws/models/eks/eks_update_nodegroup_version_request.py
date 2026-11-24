from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_launch_template_specification import EKSLaunchTemplateSpecification


class EKSUpdateNodegroupVersionRequest(BaseModel):
    clusterName: StrictStr
    nodegroupName: StrictStr
    version: StrictStr | None = None
    releaseVersion: StrictStr | None = None
    launchTemplate: EKSLaunchTemplateSpecification | None = None
    force: StrictBool | None = None
    clientRequestToken: StrictStr | None = None
