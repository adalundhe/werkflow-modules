from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_amazon_code_guru_profiler_integration import DevOpsGuruAmazonCodeGuruProfilerIntegration


class DevOpsGuruEventSourcesConfig(BaseModel):
    AmazonCodeGuruProfiler: DevOpsGuruAmazonCodeGuruProfilerIntegration | None = None
