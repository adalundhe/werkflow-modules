import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)
from werkflow_aws.models.athena import (
    AthenaCreateDataCatalogRequest,
    AthenaCreateDataCatalogResponse,
    AthenaCreateNamedQueryRequest,
    AthenaCreateNamedQueryResponse,
    AthenaCreatePreparedStatementRequest,
    AthenaCreatePreparedStatementResponse,
    AthenaGetCalculationExectutionCodeRequest,
    AthenaGetCalculationExecutionCodeResponse,
    AthenaGetCalculationExecutionRequest,
    AthenaGetCalculationExecutionResponse,
    AthenaGetCalculationExecutionStatusRequest,
    AthenaGetCalculationExecutionStatusResponse,
    AthenaGetDataCatalogRequest,
    AthenaGetDataCatalogResponse,
    AthenaGetDatabaseRequest,
    AthenaGetDatabaseResponse,
    AthenaGetNamedQueryRequest,
    AthenaGetNamedQueryResponse,
    AthenaGetPreparedStatementRequest,
    AthenaGetPreparedStatementResponse,
    AthenaGetQueryExecutionRequest,
    AthenaGetQueryExecutionResponse,
    AthenaGetQueryResultsRequest,
    AthenaGetQueryResultsResponse,
    AthenaGetSessionRequest,
    AthenaGetSessionResponse,
    AthenaGetSessionStatusRequest,
    AthenaGetSessionStatusResponse,
    AthenaListNamedQueriesRequest,
    AthenaListNamedQueriesResponse,
    AthenaListQueryExecutionsRequest,
    AthenaListQueryExecutionsResponse,
    AthenaListDatabasesRequest,
    AthenaListDatabasesResponse,
    AthenaListDataCatalogsRequest,
    AthenaListDataCatalogsResponse,
    AthenaListPreparedStatementsRequest,
    AthenaListPreparedStatementsResponse,
    AthenaListSessionsRequest,
    AthenaListSessionsResponse,
    AthenaStartCalculationExecutionRequest,
    AthenaStartCalculationExecutionResponse,
    AthenaStartQueryExecutionRequest,
    AthenaStartQueryExecutionResponse,
    AthenaStartSessionRequest,
    AthenaStartSessionResponse,
    AthenaStopCalculationExecutionRequest,
    AthenaStopCalculationExecutionResponse,
    AthenaStopQueryExecutionRequest,
    AthenaStopQueryExecutionResponse,
    AthenaTerminateSessionRequest,
    AthenaTerminateSessionResponse,
    AthenaUpdateDataCatalogRequest,
    AthenaUpdateDataCatalogResponse,
    AthenaUpdateNamedQueryRequest,
    AthenaUpdateNamedQueryResponse,
)

from werkflow_aws.helpers import collect_paginator
from werkflow_aws.types import AthenaClient

from werkflow_system import System


class AWSAthena:
    
    def __init__(self) -> None:
        self._system = System()

        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 'Athena'
        self._regions = AWSRegionMap()
    
    async def sso(
        self,
        profile_name: str,
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            None,
            functools.partial(
                boto3.setup_default_session,
                profile_name=profile_name
            )
        )

        self._client: AthenaClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'athena',
            )
        )

    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: RegionName,
    ):
        
        aws_region = self._regions.get(region)

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._client: AthenaClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'athena',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    async def create_data_catalog(
        self,
        request: AthenaCreateDataCatalogRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.create_data_catalog,
                **dumped
            )
        )

        return AthenaCreateDataCatalogResponse(**response)
    

    async def create_named_query(
        self,
        request: AthenaCreateNamedQueryRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.create_named_query,
                **dumped
            )
        )

        return AthenaCreateNamedQueryResponse(**response)
    
    async def create_prepared_statement(
        self,
        request: AthenaCreatePreparedStatementRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.create_prepared_statement,
                **dumped
            )
        )

        return AthenaCreatePreparedStatementResponse(**response)
    
    async def get_calculation_execution_code(
        self,
        request: AthenaGetCalculationExectutionCodeRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_calculation_execution_code,
                **dumped
            )
        )

        return AthenaGetCalculationExecutionCodeResponse(**response)

    async def get_calculation_execution(
        self,
        request: AthenaGetCalculationExecutionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_calculation_execution,
                **dumped
            )
        )

        return AthenaGetCalculationExecutionResponse(**response)

    async def get_calculation_execution_status(
        self,
        request: AthenaGetCalculationExecutionStatusRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_calculation_execution_status,
                **dumped
            )
        )

        return AthenaGetCalculationExecutionStatusResponse(**response)

    async def get_data_catalog(
        self,
        request: AthenaGetDataCatalogRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_data_catalog,
                **dumped
            )
        )

        return AthenaGetDataCatalogResponse(**response)
    
    async def get_database(
        self,
        request: AthenaGetDatabaseRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_database,
                **dumped
            )
        )

        return AthenaGetDatabaseResponse(**response)
    
    async def get_named_query(
        self,
        request: AthenaGetNamedQueryRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_named_query,
                **dumped
            )
        )

        return AthenaGetNamedQueryResponse(**response)
    
    async def get_prepared_statement(
        self,
        request: AthenaGetPreparedStatementRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_prepared_statement,
                **dumped
            )
        )

        return AthenaGetPreparedStatementResponse(**response)

    async def get_query_execution(
        self,
        request: AthenaGetQueryExecutionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_query_execution,
                **dumped
            )
        )

        return AthenaGetQueryExecutionResponse(**response)

    async def get_query_results(
        self,
        request: AthenaGetQueryResultsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_query_results,
                **dumped
            )
        )

        return AthenaGetQueryResultsResponse(**response)

    async def get_session_request(
        self,
        request: AthenaGetSessionRequest,
    ):    
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_session,
                **dumped
            )
        )

        return AthenaGetSessionResponse(**response)
    
    async def get_session_status_request(
        self,
        request: AthenaGetSessionStatusRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_session_status,
                **dumped
            )
        )

        return AthenaGetSessionStatusResponse(**response)

    async def list_databases(
        self,
        request: AthenaListDatabasesRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_databases,
                **dumped
            )
        )

        return AthenaListDatabasesResponse(**response)

    async def list_databases_paginated(
        self,
        request: AthenaListDatabasesRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_databases',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            AthenaListDatabasesResponse(**res) for res in results
        ]
    
    async def list_data_catalogs(
        self,
        request: AthenaListDataCatalogsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_data_catalogs,
                **dumped
            )
        )

        return AthenaListDataCatalogsResponse(**response)

    async def list_data_catalogs_paginated(
        self,
        request: AthenaListDataCatalogsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_data_catalogs',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            AthenaListDataCatalogsResponse(**res) for res in results
        ]

    async def list_named_queries(
        self,
        request: AthenaListNamedQueriesRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_named_queries,
                **dumped
            )
        )

        return AthenaListNamedQueriesResponse(**response)
    
    async def list_named_queries_paginated(
        self,
        request: AthenaListNamedQueriesRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_named_queries',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            AthenaListNamedQueriesResponse(**res) for res in results
        ]

    async def list_prepared_statements(
        self,
        request: AthenaListPreparedStatementsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_prepared_statements,
                **dumped
            )
        )

        return AthenaListPreparedStatementsResponse(**response)
    
    async def list_prepared_statements_paginated(
        self,
        request: AthenaListPreparedStatementsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_prepared_statements',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            AthenaListPreparedStatementsResponse(**res) for res in results
        ]

    async def list_query_executions(
        self,
        request: AthenaListQueryExecutionsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_query_executions,
                **dumped
            )
        )

        return AthenaListQueryExecutionsResponse(**response)
    
    async def list_query_executions_paginated(
        self,
        request: AthenaListQueryExecutionsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_query_executions',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            AthenaListQueryExecutionsResponse(**res) for res in results
        ]
    
    async def list_sessions(
        self,
        request: AthenaListSessionsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_sessions,
                **dumped
            )
        )

        return AthenaListSessionsResponse(**response)
        
    async def list_sessions_paginated(
        self,
        request: AthenaListSessionsRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_sessions',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            AthenaListSessionsResponse(**res) for res in results
        ]

    async def start_calculation_execution(
        self,
        request: AthenaStartCalculationExecutionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.start_calculation_execution,
                **dumped
            )
        )

        return AthenaStartCalculationExecutionResponse(**response)  

    async def start_query_execution(
        self,
        request: AthenaStartQueryExecutionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.start_query_execution,
                **dumped
            )
        )

        return AthenaStartQueryExecutionResponse(**response) 

    async def start_session(
        self,
        request: AthenaStartSessionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.start_session,
                **dumped
            )
        )

        return AthenaStartSessionResponse(**response)   
    
    async def stop_calculation_execution(
        self,
        request: AthenaStopCalculationExecutionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)
        
        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.stop_calculation_execution,
                **dumped
            )
        )

        return AthenaStopCalculationExecutionResponse(**response)
    
    async def stop_query_execution(
        self,
        request: AthenaStopQueryExecutionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)
        
        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.stop_query_execution,
                **dumped
            )
        )

        return AthenaStopQueryExecutionResponse(**response)
    
    async def terminate_session(
        self,
        request: AthenaTerminateSessionRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.terminate_session,
                **dumped
            )
        )

        return AthenaTerminateSessionResponse(**response)
    
    async def update_data_catalog(
        self,
        request: AthenaUpdateDataCatalogRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.update_data_catalog,
                **dumped
            )
        )

        return AthenaUpdateDataCatalogResponse(**response)
    
    async def update_named_query(
        self,
        request: AthenaUpdateNamedQueryRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.update_named_query,
                **dumped
            )
        )

        return AthenaUpdateNamedQueryResponse(**response)
    
    async def close(self):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client:
            await self._loop.run_in_executor(
                None,
                self._client.close
            )

        await self._system.close()
        self._executor.shutdown()

    def abort(self):
        self._client.close()
        self._system.abort()
        self._executor.shutdown()