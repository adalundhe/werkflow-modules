from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ecr_package_vulnerability_details import ECRPackageVulnerabilityDetails
from .ecr_remediation import ECRRemediation
from .ecr_resource import ECRResource
from .ecr_score_details import ECRScoreDetails


class ECREnhancedImageScanFinding(BaseModel):
    awsAccountId: StrictStr | None = None
    description: StrictStr | None = None
    findingArn: StrictStr | None = None
    firstObservedAt: datetime.datetime | StrictStr | None = None
    lastObservedAt: datetime.datetime | StrictStr | None = None
    packageVulnerabilityDetails: ECRPackageVulnerabilityDetails | None = None
    remediation: ECRRemediation | None = None
    resources: list[ECRResource] | None = None
    score: StrictFloat | StrictInt | None = None
    scoreDetails: ECRScoreDetails | None = None
    severity: StrictStr | None = None
    status: StrictStr | None = None
    title: StrictStr | None = None
    type: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    fixAvailable: StrictStr | None = None
    exploitAvailable: StrictStr | None = None
