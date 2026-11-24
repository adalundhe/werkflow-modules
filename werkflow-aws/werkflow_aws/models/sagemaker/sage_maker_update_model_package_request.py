from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_additional_inference_specification_definition import SageMakerAdditionalInferenceSpecificationDefinition
from .sage_maker_inference_specification import SageMakerInferenceSpecification
from .sage_maker_model_life_cycle import SageMakerModelLifeCycle
from .sage_maker_model_package_model_card import SageMakerModelPackageModelCard


class SageMakerUpdateModelPackageRequest(BaseModel):
    ModelPackageArn: StrictStr
    ModelApprovalStatus: Literal['Approved', 'Rejected', 'PendingManualApproval'] | None = None
    ModelPackageRegistrationType: Literal['Logged', 'Registered'] | None = None
    ApprovalDescription: StrictStr | None = None
    CustomerMetadataProperties: dict[StrictStr, StrictStr] | None = None
    CustomerMetadataPropertiesToRemove: list[StrictStr] | None = None
    AdditionalInferenceSpecificationsToAdd: list[SageMakerAdditionalInferenceSpecificationDefinition] | None = None
    InferenceSpecification: SageMakerInferenceSpecification | None = None
    SourceUri: StrictStr | None = None
    ModelCard: SageMakerModelPackageModelCard | None = None
    ModelLifeCycle: SageMakerModelLifeCycle | None = None
    ClientToken: StrictStr | None = None
