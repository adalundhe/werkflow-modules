from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_additional_enis import SageMakerAdditionalEnis


class SageMakerInstanceRequirementsEniConfiguration(BaseModel):
    CustomerEni: StrictStr | None = None
    AdditionalEnis: SageMakerAdditionalEnis | None = None
