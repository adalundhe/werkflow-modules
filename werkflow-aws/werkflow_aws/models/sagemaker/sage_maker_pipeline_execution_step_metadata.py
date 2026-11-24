from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_athena_step_metadata import SageMakerAthenaStepMetadata
from .sage_maker_auto_ml_job_step_metadata import SageMakerAutoMLJobStepMetadata
from .sage_maker_bedrock_custom_model_deployment_metadata import SageMakerBedrockCustomModelDeploymentMetadata
from .sage_maker_bedrock_custom_model_metadata import SageMakerBedrockCustomModelMetadata
from .sage_maker_bedrock_model_import_metadata import SageMakerBedrockModelImportMetadata
from .sage_maker_bedrock_provisioned_model_throughput_metadata import SageMakerBedrockProvisionedModelThroughputMetadata
from .sage_maker_callback_step_metadata import SageMakerCallbackStepMetadata
from .sage_maker_clarify_check_step_metadata import SageMakerClarifyCheckStepMetadata
from .sage_maker_cleanup_step_metadata import SageMakerCleanupStepMetadata
from .sage_maker_condition_step_metadata import SageMakerConditionStepMetadata
from .sage_maker_emr_serverless_step_metadata import SageMakerEMRServerlessStepMetadata
from .sage_maker_emr_step_metadata import SageMakerEMRStepMetadata
from .sage_maker_endpoint_config_step_metadata import SageMakerEndpointConfigStepMetadata
from .sage_maker_endpoint_step_metadata import SageMakerEndpointStepMetadata
from .sage_maker_fail_step_metadata import SageMakerFailStepMetadata
from .sage_maker_for_each_step_metadata import SageMakerForEachStepMetadata
from .sage_maker_hub_content_step_metadata import SageMakerHubContentStepMetadata
from .sage_maker_inference_component_metadata import SageMakerInferenceComponentMetadata
from .sage_maker_job_step_metadata import SageMakerJobStepMetadata
from .sage_maker_lambda_step_metadata import SageMakerLambdaStepMetadata
from .sage_maker_lineage_metadata import SageMakerLineageMetadata
from .sage_maker_model_step_metadata import SageMakerModelStepMetadata
from .sage_maker_processing_job_step_metadata import SageMakerProcessingJobStepMetadata
from .sage_maker_quality_check_step_metadata import SageMakerQualityCheckStepMetadata
from .sage_maker_register_model_step_metadata import SageMakerRegisterModelStepMetadata
from .sage_maker_training_job_step_metadata import SageMakerTrainingJobStepMetadata
from .sage_maker_transform_job_step_metadata import SageMakerTransformJobStepMetadata
from .sage_maker_tuning_job_step_meta_data import SageMakerTuningJobStepMetaData


class SageMakerPipelineExecutionStepMetadata(BaseModel):
    TrainingJob: SageMakerTrainingJobStepMetadata | None = None
    ProcessingJob: SageMakerProcessingJobStepMetadata | None = None
    TransformJob: SageMakerTransformJobStepMetadata | None = None
    TuningJob: SageMakerTuningJobStepMetaData | None = None
    Model: SageMakerModelStepMetadata | None = None
    RegisterModel: SageMakerRegisterModelStepMetadata | None = None
    Condition: SageMakerConditionStepMetadata | None = None
    Callback: SageMakerCallbackStepMetadata | None = None
    Lambda: SageMakerLambdaStepMetadata | None = None
    EMR: SageMakerEMRStepMetadata | None = None
    EMRServerless: SageMakerEMRServerlessStepMetadata | None = None
    QualityCheck: SageMakerQualityCheckStepMetadata | None = None
    ClarifyCheck: SageMakerClarifyCheckStepMetadata | None = None
    Fail: SageMakerFailStepMetadata | None = None
    AutoMLJob: SageMakerAutoMLJobStepMetadata | None = None
    Endpoint: SageMakerEndpointStepMetadata | None = None
    EndpointConfig: SageMakerEndpointConfigStepMetadata | None = None
    BedrockCustomModel: SageMakerBedrockCustomModelMetadata | None = None
    BedrockCustomModelDeployment: SageMakerBedrockCustomModelDeploymentMetadata | None = None
    BedrockProvisionedModelThroughput: SageMakerBedrockProvisionedModelThroughputMetadata | None = None
    BedrockModelImport: SageMakerBedrockModelImportMetadata | None = None
    InferenceComponent: SageMakerInferenceComponentMetadata | None = None
    Lineage: SageMakerLineageMetadata | None = None
    Job: SageMakerJobStepMetadata | None = None
    Athena: SageMakerAthenaStepMetadata | None = None
    Cleanup: SageMakerCleanupStepMetadata | None = None
    ForEach: SageMakerForEachStepMetadata | None = None
    HubContent: SageMakerHubContentStepMetadata | None = None
