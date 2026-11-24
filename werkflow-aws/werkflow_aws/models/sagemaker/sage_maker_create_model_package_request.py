from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_additional_inference_specification_definition import SageMakerAdditionalInferenceSpecificationDefinition
from .sage_maker_drift_check_baselines import SageMakerDriftCheckBaselines
from .sage_maker_inference_specification import SageMakerInferenceSpecification
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_model_life_cycle import SageMakerModelLifeCycle
from .sage_maker_model_metrics import SageMakerModelMetrics
from .sage_maker_model_package_model_card import SageMakerModelPackageModelCard
from .sage_maker_model_package_security_config import SageMakerModelPackageSecurityConfig
from .sage_maker_model_package_validation_specification import SageMakerModelPackageValidationSpecification
from .sage_maker_source_algorithm_specification import SageMakerSourceAlgorithmSpecification
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateModelPackageRequest(BaseModel):
    ModelPackageName: StrictStr | None = None
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageDescription: StrictStr | None = None
    ModelPackageRegistrationType: Literal['Logged', 'Registered'] | None = None
    InferenceSpecification: SageMakerInferenceSpecification | None = None
    ValidationSpecification: SageMakerModelPackageValidationSpecification | None = None
    SourceAlgorithmSpecification: SageMakerSourceAlgorithmSpecification | None = None
    CertifyForMarketplace: StrictBool | None = None
    Tags: list[SageMakerTagModel] | None = None
    ModelApprovalStatus: Literal['Approved', 'Rejected', 'PendingManualApproval'] | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    ModelMetrics: SageMakerModelMetrics | None = None
    ClientToken: StrictStr | None = None
    Domain: StrictStr | None = None
    Task: StrictStr | None = None
    SamplePayloadUrl: StrictStr | None = None
    CustomerMetadataProperties: dict[StrictStr, StrictStr] | None = None
    DriftCheckBaselines: SageMakerDriftCheckBaselines | None = None
    AdditionalInferenceSpecifications: list[SageMakerAdditionalInferenceSpecificationDefinition] | None = None
    SkipModelValidation: Literal['All', 'None'] | None = None
    SourceUri: StrictStr | None = None
    SecurityConfig: SageMakerModelPackageSecurityConfig | None = None
    ModelCard: SageMakerModelPackageModelCard | None = None
    ModelLifeCycle: SageMakerModelLifeCycle | None = None
    ManagedStorageType: Literal['Restricted'] | None = None
