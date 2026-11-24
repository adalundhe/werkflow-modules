from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_engine_version_model import AthenaEngineVersionModel
from .athena_managed_query_results_configuration_model import AthenaManagedQueryResultsConfigurationModel
from .athena_query_execution_context_model import AthenaQueryExecutionContextModel
from .athena_query_execution_statistics import AthenaQueryExecutionStatistics
from .athena_query_execution_status import AthenaQueryExecutionStatus
from .athena_query_results_s3_access_grants_configuration_model import AthenaQueryResultsS3AccessGrantsConfigurationModel
from .athena_result_configuration_model import AthenaResultConfigurationModel
from .athena_result_reuse_configuration_model import AthenaResultReuseConfigurationModel


class AthenaQueryExecutionModel(BaseModel):
    QueryExecutionId: StrictStr | None = None
    Query: StrictStr | None = None
    StatementType: StrictStr | None = None
    ManagedQueryResultsConfiguration: AthenaManagedQueryResultsConfigurationModel | None = None
    ResultConfiguration: AthenaResultConfigurationModel | None = None
    ResultReuseConfiguration: AthenaResultReuseConfigurationModel | None = None
    QueryExecutionContext: AthenaQueryExecutionContextModel | None = None
    Status: AthenaQueryExecutionStatus | None = None
    Statistics: AthenaQueryExecutionStatistics | None = None
    WorkGroup: StrictStr | None = None
    EngineVersion: AthenaEngineVersionModel | None = None
    ExecutionParameters: list[StrictStr] | None = None
    SubstatementType: StrictStr | None = None
    QueryResultsS3AccessGrantsConfiguration: AthenaQueryResultsS3AccessGrantsConfigurationModel | None = None
