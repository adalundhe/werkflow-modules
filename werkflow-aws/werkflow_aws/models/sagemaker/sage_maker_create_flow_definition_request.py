from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_flow_definition_output_config import SageMakerFlowDefinitionOutputConfig
from .sage_maker_human_loop_activation_config import SageMakerHumanLoopActivationConfig
from .sage_maker_human_loop_config import SageMakerHumanLoopConfig
from .sage_maker_human_loop_request_source import SageMakerHumanLoopRequestSource
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateFlowDefinitionRequest(BaseModel):
    FlowDefinitionName: StrictStr
    OutputConfig: SageMakerFlowDefinitionOutputConfig
    RoleArn: StrictStr
    HumanLoopRequestSource: SageMakerHumanLoopRequestSource | None = None
    HumanLoopActivationConfig: SageMakerHumanLoopActivationConfig | None = None
    HumanLoopConfig: SageMakerHumanLoopConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
