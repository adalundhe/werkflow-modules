from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_parallelism_configuration_model import SageMakerParallelismConfigurationModel
from .sage_maker_pipeline_definition_s3_location import SageMakerPipelineDefinitionS3Location
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreatePipelineRequest(BaseModel):
    PipelineName: StrictStr
    ClientRequestToken: StrictStr
    RoleArn: StrictStr
    PipelineDisplayName: StrictStr | None = None
    PipelineDefinition: StrictStr | None = None
    PipelineDefinitionS3Location: SageMakerPipelineDefinitionS3Location | None = None
    PipelineDescription: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    ParallelismConfiguration: SageMakerParallelismConfigurationModel | None = None
    PipelineVersionAliases: list[StrictStr] | None = None
