from __future__ import annotations
from pydantic import BaseModel
from .personalize_hpo_objective import PersonalizeHPOObjective
from .personalize_hpo_resource_config import PersonalizeHPOResourceConfig
from .personalize_hyper_parameter_ranges import PersonalizeHyperParameterRanges


class PersonalizeHPOConfig(BaseModel):
    hpoObjective: PersonalizeHPOObjective | None = None
    hpoResourceConfig: PersonalizeHPOResourceConfig | None = None
    algorithmHyperParameterRanges: PersonalizeHyperParameterRanges | None = None
