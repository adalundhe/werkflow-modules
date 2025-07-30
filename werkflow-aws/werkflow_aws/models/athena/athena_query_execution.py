from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_engine_version import AthenaEngineVersion
from .athena_managed_query_results_configuration import AthenaManagedQueryResultsConfiguration
from .athena_statement_type import AthenaStatementType
from .athena_result_configuration import AthenaResultConfigruation
from .athena_result_reuse_configuration import AthenaResultReuseConfiguration
from .athena_query_execution_context import AthenaQueryExecutionContext
from .athena_query_status import AthenaQueryStatus
from .athena_query_statistics import AthenaQueryStatistics
from .athena_query_results_s3_access_grants_configruation import AthenaQueryResultsS3AccessGrantsConfiguration


class AthenaQueryExecution(BaseModel):
    QueryExecutionId: StrictStr
    Query: StrictStr
    StatementType: AthenaStatementType
    ManagedQueryResultsConfiguration: AthenaManagedQueryResultsConfiguration
    ResultConfiguration: AthenaResultConfigruation
    ResultReuseConfiguration: AthenaResultReuseConfiguration
    QueryExecutionContext: AthenaQueryExecutionContext
    Status: AthenaQueryStatus
    Statistics: AthenaQueryStatistics
    WorkGroup: StrictStr
    EngineVersion: AthenaEngineVersion
    ExecutionParameters: list[StrictStr]
    SubstatementType: StrictStr
    QueryResultsS3AccessGrantsConfiguration: AthenaQueryResultsS3AccessGrantsConfiguration