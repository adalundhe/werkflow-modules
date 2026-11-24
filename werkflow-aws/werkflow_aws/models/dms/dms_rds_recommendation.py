from __future__ import annotations
from pydantic import BaseModel
from .dms_rds_configuration import DMSRdsConfiguration
from .dms_rds_requirements import DMSRdsRequirements


class DMSRdsRecommendation(BaseModel):
    RequirementsToTarget: DMSRdsRequirements | None = None
    TargetConfiguration: DMSRdsConfiguration | None = None
