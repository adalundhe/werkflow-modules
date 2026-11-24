from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyS3Analysis(BaseModel):
    FindingSubtype: StrictStr | None = None
    EffectivePermission: StrictStr | None = None
    BlockPublicAccessSettings: StrictStr | None = None
    Exposure: StrictStr | None = None
    UserAgent: StrictStr | None = None
    UserAgentClassification: StrictStr | None = None
    SourceIp: StrictStr | None = None
    IpReputation: StrictStr | None = None
    ActorAssessment: StrictStr | None = None
    S3ApiActivity: StrictStr | None = None
    SourceContext: StrictStr | None = None
    AuthorizationAssessment: StrictStr | None = None
