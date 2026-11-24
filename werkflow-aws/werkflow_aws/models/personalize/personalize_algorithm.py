from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .personalize_algorithm_image import PersonalizeAlgorithmImage
from .personalize_default_hyper_parameter_ranges import PersonalizeDefaultHyperParameterRanges


class PersonalizeAlgorithm(BaseModel):
    name: StrictStr | None = None
    algorithmArn: StrictStr | None = None
    algorithmImage: PersonalizeAlgorithmImage | None = None
    defaultHyperParameters: dict[StrictStr, StrictStr] | None = None
    defaultHyperParameterRanges: PersonalizeDefaultHyperParameterRanges | None = None
    defaultResourceConfig: dict[StrictStr, StrictStr] | None = None
    trainingInputMode: StrictStr | None = None
    roleArn: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
