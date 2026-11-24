from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_additional_enis import SageMakerAdditionalEnis
from .sage_maker_capacity_reservation import SageMakerCapacityReservation
from .sage_maker_instance_requirements_eni_configuration import SageMakerInstanceRequirementsEniConfiguration


class SageMakerInstanceMetadata(BaseModel):
    CustomerEni: StrictStr | None = None
    AdditionalEnis: SageMakerAdditionalEnis | None = None
    InstanceRequirementsEniConfigurations: list[SageMakerInstanceRequirementsEniConfiguration] | None = None
    CapacityReservation: SageMakerCapacityReservation | None = None
    FailureMessage: StrictStr | None = None
    LcsExecutionState: StrictStr | None = None
    NodeLogicalId: StrictStr | None = None
