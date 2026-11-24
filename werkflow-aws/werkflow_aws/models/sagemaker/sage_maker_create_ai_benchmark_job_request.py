from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_benchmark_network_config import SageMakerAIBenchmarkNetworkConfig
from .sage_maker_ai_benchmark_output_config import SageMakerAIBenchmarkOutputConfig
from .sage_maker_ai_benchmark_target import SageMakerAIBenchmarkTarget
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateAIBenchmarkJobRequest(BaseModel):
    AIBenchmarkJobName: StrictStr
    BenchmarkTarget: SageMakerAIBenchmarkTarget
    OutputConfig: SageMakerAIBenchmarkOutputConfig
    AIWorkloadConfigIdentifier: StrictStr
    RoleArn: StrictStr
    NetworkConfig: SageMakerAIBenchmarkNetworkConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
