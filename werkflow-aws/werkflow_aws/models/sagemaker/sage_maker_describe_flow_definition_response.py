from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_flow_definition_output_config import SageMakerFlowDefinitionOutputConfig
from .sage_maker_human_loop_activation_config import SageMakerHumanLoopActivationConfig
from .sage_maker_human_loop_config import SageMakerHumanLoopConfig
from .sage_maker_human_loop_request_source import SageMakerHumanLoopRequestSource


class SageMakerDescribeFlowDefinitionResponse(BaseModel):
    FlowDefinitionArn: StrictStr | None = None
    FlowDefinitionName: StrictStr | None = None
    FlowDefinitionStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    HumanLoopRequestSource: SageMakerHumanLoopRequestSource | None = None
    HumanLoopActivationConfig: SageMakerHumanLoopActivationConfig | None = None
    HumanLoopConfig: SageMakerHumanLoopConfig | None = None
    OutputConfig: SageMakerFlowDefinitionOutputConfig | None = None
    RoleArn: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
