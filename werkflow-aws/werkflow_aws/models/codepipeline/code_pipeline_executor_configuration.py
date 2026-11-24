from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_job_worker_executor_configuration import CodePipelineJobWorkerExecutorConfiguration
from .code_pipeline_lambda_executor_configuration import CodePipelineLambdaExecutorConfiguration


class CodePipelineExecutorConfiguration(BaseModel):
    lambdaExecutorConfiguration: CodePipelineLambdaExecutorConfiguration | None = None
    jobWorkerExecutorConfiguration: CodePipelineJobWorkerExecutorConfiguration | None = None
