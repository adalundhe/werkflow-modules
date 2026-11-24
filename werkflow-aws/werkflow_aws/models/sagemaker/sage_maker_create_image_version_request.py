from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerCreateImageVersionRequest(BaseModel):
    BaseImage: StrictStr
    ClientToken: StrictStr
    ImageName: StrictStr
    Aliases: list[StrictStr] | None = None
    VendorGuidance: Literal['NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED', 'ARCHIVED'] | None = None
    JobType: Literal['TRAINING', 'INFERENCE', 'NOTEBOOK_KERNEL'] | None = None
    MLFramework: StrictStr | None = None
    ProgrammingLang: StrictStr | None = None
    Processor: Literal['CPU', 'GPU'] | None = None
    Horovod: StrictBool | None = None
    ReleaseNotes: StrictStr | None = None
