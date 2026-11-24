from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_additional_inference_specification_definition import SageMakerAdditionalInferenceSpecificationDefinition
from .sage_maker_drift_check_baselines import SageMakerDriftCheckBaselines
from .sage_maker_inference_specification import SageMakerInferenceSpecification
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_model_life_cycle import SageMakerModelLifeCycle
from .sage_maker_model_metrics import SageMakerModelMetrics
from .sage_maker_model_package_model_card import SageMakerModelPackageModelCard
from .sage_maker_model_package_security_config import SageMakerModelPackageSecurityConfig
from .sage_maker_model_package_status_details import SageMakerModelPackageStatusDetails
from .sage_maker_model_package_validation_specification import SageMakerModelPackageValidationSpecification
from .sage_maker_source_algorithm_specification import SageMakerSourceAlgorithmSpecification
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeModelPackageResponse(BaseModel):
    ModelPackageName: StrictStr | None = None
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageVersion: StrictInt | None = None
    ModelPackageRegistrationType: StrictStr | None = None
    ModelPackageArn: StrictStr | None = None
    ModelPackageDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    InferenceSpecification: SageMakerInferenceSpecification | None = None
    SourceAlgorithmSpecification: SageMakerSourceAlgorithmSpecification | None = None
    ValidationSpecification: SageMakerModelPackageValidationSpecification | None = None
    ModelPackageStatus: StrictStr | None = None
    ModelPackageStatusDetails: SageMakerModelPackageStatusDetails | None = None
    CertifyForMarketplace: StrictBool | None = None
    ModelApprovalStatus: StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    ModelMetrics: SageMakerModelMetrics | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ApprovalDescription: StrictStr | None = None
    Domain: StrictStr | None = None
    Task: StrictStr | None = None
    SamplePayloadUrl: StrictStr | None = None
    CustomerMetadataProperties: dict[StrictStr, StrictStr] | None = None
    DriftCheckBaselines: SageMakerDriftCheckBaselines | None = None
    AdditionalInferenceSpecifications: list[SageMakerAdditionalInferenceSpecificationDefinition] | None = None
    SkipModelValidation: StrictStr | None = None
    SourceUri: StrictStr | None = None
    SecurityConfig: SageMakerModelPackageSecurityConfig | None = None
    ModelCard: SageMakerModelPackageModelCard | None = None
    ModelLifeCycle: SageMakerModelLifeCycle | None = None
    ManagedStorageType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
