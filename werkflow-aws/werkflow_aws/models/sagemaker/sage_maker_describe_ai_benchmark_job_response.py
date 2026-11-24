from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_benchmark_network_config import SageMakerAIBenchmarkNetworkConfig
from .sage_maker_ai_benchmark_output_result import SageMakerAIBenchmarkOutputResult
from .sage_maker_ai_benchmark_target import SageMakerAIBenchmarkTarget
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerDescribeAIBenchmarkJobResponse(BaseModel):
    AIBenchmarkJobName: StrictStr | None = None
    AIBenchmarkJobArn: StrictStr | None = None
    AIBenchmarkJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    BenchmarkTarget: SageMakerAIBenchmarkTarget | None = None
    OutputConfig: SageMakerAIBenchmarkOutputResult | None = None
    AIWorkloadConfigIdentifier: StrictStr | None = None
    RoleArn: StrictStr | None = None
    NetworkConfig: SageMakerAIBenchmarkNetworkConfig | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
