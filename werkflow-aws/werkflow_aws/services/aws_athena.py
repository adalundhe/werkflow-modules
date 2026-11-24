from werkflow_aws.models.athena import (
    AthenaCreateDataCatalogRequest,
    AthenaCreateDataCatalogResponse,
    AthenaCreateNamedQueryRequest,
    AthenaCreateNamedQueryResponse,
    AthenaCreatePreparedStatementRequest,
    AthenaCreatePreparedStatementResponse,
    AthenaDeleteDataCatalogRequest,
    AthenaDeleteDataCatalogResponse,
    AthenaDeleteNamedQueryRequest,
    AthenaDeleteNamedQueryResponse,
    AthenaDeletePreparedStatementRequest,
    AthenaDeletePreparedStatementResponse,
    AthenaGetCalculationExecutionCodeRequest,
    AthenaGetCalculationExecutionCodeResponse,
    AthenaGetCalculationExecutionRequest,
    AthenaGetCalculationExecutionResponse,
    AthenaGetCalculationExecutionStatusRequest,
    AthenaGetCalculationExecutionStatusResponse,
    AthenaGetDatabaseRequest,
    AthenaGetDatabaseResponse,
    AthenaGetDataCatalogRequest,
    AthenaGetDataCatalogResponse,
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
    AthenaListDatabasesRequest,
    AthenaListDatabasesResponse,
    AthenaListDataCatalogsRequest,
    AthenaListDataCatalogsResponse,
    AthenaListNamedQueriesRequest,
    AthenaListNamedQueriesResponse,
    AthenaListPreparedStatementsRequest,
    AthenaListPreparedStatementsResponse,
    AthenaListQueryExecutionsRequest,
    AthenaListQueryExecutionsResponse,
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
from werkflow_aws.types import AthenaClient
from .base import AWSBaseService
from werkflow_aws.models.athena import (
    AthenaBatchGetNamedQueryRequest,
    AthenaBatchGetNamedQueryResponse,
    AthenaBatchGetPreparedStatementRequest,
    AthenaBatchGetPreparedStatementResponse,
    AthenaBatchGetQueryExecutionRequest,
    AthenaBatchGetQueryExecutionResponse,
    AthenaCancelCapacityReservationRequest,
    AthenaCancelCapacityReservationResponse,
    AthenaCreateCapacityReservationRequest,
    AthenaCreateCapacityReservationResponse,
    AthenaCreateNotebookRequest,
    AthenaCreateNotebookResponse,
    AthenaCreatePresignedNotebookUrlRequest,
    AthenaCreatePresignedNotebookUrlResponse,
    AthenaCreateSystemTableConfigurationRequest,
    AthenaCreateSystemTableConfigurationResponse,
    AthenaCreateWorkGroupRequest,
    AthenaCreateWorkGroupResponse,
    AthenaDeleteCapacityReservationRequest,
    AthenaDeleteCapacityReservationResponse,
    AthenaDeleteNotebookRequest,
    AthenaDeleteNotebookResponse,
    AthenaDeleteSystemTableConfigurationRequest,
    AthenaDeleteSystemTableConfigurationResponse,
    AthenaDeleteWorkGroupRequest,
    AthenaDeleteWorkGroupResponse,
    AthenaExportNotebookRequest,
    AthenaExportNotebookResponse,
    AthenaGetCapacityAssignmentConfigurationRequest,
    AthenaGetCapacityAssignmentConfigurationResponse,
    AthenaGetCapacityReservationRequest,
    AthenaGetCapacityReservationResponse,
    AthenaGetNotebookMetadataRequest,
    AthenaGetNotebookMetadataResponse,
    AthenaGetQueryRuntimeStatisticsRequest,
    AthenaGetQueryRuntimeStatisticsResponse,
    AthenaGetResourceDashboardRequest,
    AthenaGetResourceDashboardResponse,
    AthenaGetSessionEndpointRequest,
    AthenaGetSessionEndpointResponse,
    AthenaGetSystemTableConfigurationRequest,
    AthenaGetSystemTableConfigurationResponse,
    AthenaGetTableMetadataRequest,
    AthenaGetTableMetadataResponse,
    AthenaGetWorkGroupRequest,
    AthenaGetWorkGroupResponse,
    AthenaImportNotebookRequest,
    AthenaImportNotebookResponse,
    AthenaListApplicationDPUSizesRequest,
    AthenaListApplicationDPUSizesResponse,
    AthenaListCalculationExecutionsRequest,
    AthenaListCalculationExecutionsResponse,
    AthenaListCapacityReservationsRequest,
    AthenaListCapacityReservationsResponse,
    AthenaListEngineVersionsRequest,
    AthenaListEngineVersionsResponse,
    AthenaListExecutorsRequest,
    AthenaListExecutorsResponse,
    AthenaListNotebookMetadataRequest,
    AthenaListNotebookMetadataResponse,
    AthenaListNotebookSessionsRequest,
    AthenaListNotebookSessionsResponse,
    AthenaListSystemTableStatusesRequest,
    AthenaListSystemTableStatusesResponse,
    AthenaListTableMetadataRequest,
    AthenaListTableMetadataResponse,
    AthenaListTagsForResourceRequest,
    AthenaListTagsForResourceResponse,
    AthenaListWorkGroupsRequest,
    AthenaListWorkGroupsResponse,
    AthenaPutCapacityAssignmentConfigurationRequest,
    AthenaPutCapacityAssignmentConfigurationResponse,
    AthenaTagResourceRequest,
    AthenaTagResourceResponse,
    AthenaUntagResourceRequest,
    AthenaUntagResourceResponse,
    AthenaUpdateCapacityReservationRequest,
    AthenaUpdateCapacityReservationResponse,
    AthenaUpdateNotebookMetadataRequest,
    AthenaUpdateNotebookMetadataResponse,
    AthenaUpdateNotebookRequest,
    AthenaUpdateNotebookResponse,
    AthenaUpdatePreparedStatementRequest,
    AthenaUpdatePreparedStatementResponse,
    AthenaUpdateSystemTableConfigurationRequest,
    AthenaUpdateSystemTableConfigurationResponse,
    AthenaUpdateWorkGroupRequest,
    AthenaUpdateWorkGroupResponse,
)


class AWSAthena(AWSBaseService[AthenaClient]):
    service_name = 'Athena'
    boto3_service_name = 'athena'

    def __init__(self) -> None:
        super().__init__(service_name='Athena', boto3_service_name='athena')

    async def create_data_catalog(
        self,
        request: AthenaCreateDataCatalogRequest,
    ) -> AthenaCreateDataCatalogResponse:
        client = self._require_client()
        return await self._execute(
            client.create_data_catalog,
            request,
            AthenaCreateDataCatalogResponse,
        )

    async def create_named_query(
        self,
        request: AthenaCreateNamedQueryRequest,
    ) -> AthenaCreateNamedQueryResponse:
        client = self._require_client()
        return await self._execute(
            client.create_named_query,
            request,
            AthenaCreateNamedQueryResponse,
        )

    async def create_prepared_statement(
        self,
        request: AthenaCreatePreparedStatementRequest,
    ) -> AthenaCreatePreparedStatementResponse:
        client = self._require_client()
        return await self._execute(
            client.create_prepared_statement,
            request,
            AthenaCreatePreparedStatementResponse,
        )

    async def delete_data_catalog(
        self,
        request: AthenaDeleteDataCatalogRequest,
    ) -> AthenaDeleteDataCatalogResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_data_catalog,
            request,
            AthenaDeleteDataCatalogResponse,
        )

    async def delete_named_query(
        self,
        request: AthenaDeleteNamedQueryRequest,
    ) -> AthenaDeleteNamedQueryResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_named_query,
            request,
            AthenaDeleteNamedQueryResponse,
        )

    async def delete_prepared_statement(
        self,
        request: AthenaDeletePreparedStatementRequest,
    ) -> AthenaDeletePreparedStatementResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_prepared_statement,
            request,
            AthenaDeletePreparedStatementResponse,
        )

    async def get_calculation_execution_code(
        self,
        request: AthenaGetCalculationExecutionCodeRequest,
    ) -> AthenaGetCalculationExecutionCodeResponse:
        client = self._require_client()
        return await self._execute(
            client.get_calculation_execution_code,
            request,
            AthenaGetCalculationExecutionCodeResponse,
        )

    async def get_calculation_execution(
        self,
        request: AthenaGetCalculationExecutionRequest,
    ) -> AthenaGetCalculationExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.get_calculation_execution,
            request,
            AthenaGetCalculationExecutionResponse,
        )

    async def get_calculation_execution_status(
        self,
        request: AthenaGetCalculationExecutionStatusRequest,
    ) -> AthenaGetCalculationExecutionStatusResponse:
        client = self._require_client()
        return await self._execute(
            client.get_calculation_execution_status,
            request,
            AthenaGetCalculationExecutionStatusResponse,
        )

    async def get_data_catalog(
        self,
        request: AthenaGetDataCatalogRequest,
    ) -> AthenaGetDataCatalogResponse:
        client = self._require_client()
        return await self._execute(
            client.get_data_catalog,
            request,
            AthenaGetDataCatalogResponse,
        )

    async def get_database(
        self,
        request: AthenaGetDatabaseRequest,
    ) -> AthenaGetDatabaseResponse:
        client = self._require_client()
        return await self._execute(
            client.get_database,
            request,
            AthenaGetDatabaseResponse,
        )

    async def get_named_query(
        self,
        request: AthenaGetNamedQueryRequest,
    ) -> AthenaGetNamedQueryResponse:
        client = self._require_client()
        return await self._execute(
            client.get_named_query,
            request,
            AthenaGetNamedQueryResponse,
        )

    async def get_prepared_statement(
        self,
        request: AthenaGetPreparedStatementRequest,
    ) -> AthenaGetPreparedStatementResponse:
        client = self._require_client()
        return await self._execute(
            client.get_prepared_statement,
            request,
            AthenaGetPreparedStatementResponse,
        )

    async def get_query_execution(
        self,
        request: AthenaGetQueryExecutionRequest,
    ) -> AthenaGetQueryExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.get_query_execution,
            request,
            AthenaGetQueryExecutionResponse,
        )

    async def get_query_results(
        self,
        request: AthenaGetQueryResultsRequest,
    ) -> AthenaGetQueryResultsResponse:
        client = self._require_client()
        return await self._execute(
            client.get_query_results,
            request,
            AthenaGetQueryResultsResponse,
        )

    async def get_query_results_paginated(
        self,
        request: AthenaGetQueryResultsRequest,
    ) -> list[AthenaGetQueryResultsResponse]:
        return await self._paginate(
            'get_query_results',
            request,
            AthenaGetQueryResultsResponse,
        )

    async def get_session(
        self,
        request: AthenaGetSessionRequest,
    ) -> AthenaGetSessionResponse:
        client = self._require_client()
        return await self._execute(
            client.get_session,
            request,
            AthenaGetSessionResponse,
        )

    get_session_request = get_session

    async def get_session_status(
        self,
        request: AthenaGetSessionStatusRequest,
    ) -> AthenaGetSessionStatusResponse:
        client = self._require_client()
        return await self._execute(
            client.get_session_status,
            request,
            AthenaGetSessionStatusResponse,
        )

    get_session_status_request = get_session_status

    async def list_databases(
        self,
        request: AthenaListDatabasesRequest,
    ) -> AthenaListDatabasesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_databases,
            request,
            AthenaListDatabasesResponse,
        )

    async def list_databases_paginated(
        self,
        request: AthenaListDatabasesRequest,
    ) -> list[AthenaListDatabasesResponse]:
        return await self._paginate(
            'list_databases',
            request,
            AthenaListDatabasesResponse,
        )

    async def list_data_catalogs(
        self,
        request: AthenaListDataCatalogsRequest | None = None,
    ) -> AthenaListDataCatalogsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_data_catalogs,
            request or AthenaListDataCatalogsRequest(),
            AthenaListDataCatalogsResponse,
        )

    async def list_data_catalogs_paginated(
        self,
        request: AthenaListDataCatalogsRequest | None = None,
    ) -> list[AthenaListDataCatalogsResponse]:
        return await self._paginate(
            'list_data_catalogs',
            request or AthenaListDataCatalogsRequest(),
            AthenaListDataCatalogsResponse,
        )

    async def list_named_queries(
        self,
        request: AthenaListNamedQueriesRequest | None = None,
    ) -> AthenaListNamedQueriesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_named_queries,
            request or AthenaListNamedQueriesRequest(),
            AthenaListNamedQueriesResponse,
        )

    async def list_named_queries_paginated(
        self,
        request: AthenaListNamedQueriesRequest | None = None,
    ) -> list[AthenaListNamedQueriesResponse]:
        return await self._paginate(
            'list_named_queries',
            request or AthenaListNamedQueriesRequest(),
            AthenaListNamedQueriesResponse,
        )

    async def list_prepared_statements(
        self,
        request: AthenaListPreparedStatementsRequest,
    ) -> AthenaListPreparedStatementsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_prepared_statements,
            request,
            AthenaListPreparedStatementsResponse,
        )

    async def list_prepared_statements_paginated(
        self,
        request: AthenaListPreparedStatementsRequest,
    ) -> list[AthenaListPreparedStatementsResponse]:
        return await self._paginate(
            'list_prepared_statements',
            request,
            AthenaListPreparedStatementsResponse,
        )

    async def list_query_executions(
        self,
        request: AthenaListQueryExecutionsRequest | None = None,
    ) -> AthenaListQueryExecutionsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_query_executions,
            request or AthenaListQueryExecutionsRequest(),
            AthenaListQueryExecutionsResponse,
        )

    async def list_query_executions_paginated(
        self,
        request: AthenaListQueryExecutionsRequest | None = None,
    ) -> list[AthenaListQueryExecutionsResponse]:
        return await self._paginate(
            'list_query_executions',
            request or AthenaListQueryExecutionsRequest(),
            AthenaListQueryExecutionsResponse,
        )

    async def list_sessions(
        self,
        request: AthenaListSessionsRequest,
    ) -> AthenaListSessionsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_sessions,
            request,
            AthenaListSessionsResponse,
        )

    async def list_sessions_paginated(
        self,
        request: AthenaListSessionsRequest,
    ) -> list[AthenaListSessionsResponse]:
        return await self._paginate(
            'list_sessions',
            request,
            AthenaListSessionsResponse,
        )

    async def start_calculation_execution(
        self,
        request: AthenaStartCalculationExecutionRequest,
    ) -> AthenaStartCalculationExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.start_calculation_execution,
            request,
            AthenaStartCalculationExecutionResponse,
        )

    async def start_query_execution(
        self,
        request: AthenaStartQueryExecutionRequest,
    ) -> AthenaStartQueryExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.start_query_execution,
            request,
            AthenaStartQueryExecutionResponse,
        )

    async def start_session(
        self,
        request: AthenaStartSessionRequest,
    ) -> AthenaStartSessionResponse:
        client = self._require_client()
        return await self._execute(
            client.start_session,
            request,
            AthenaStartSessionResponse,
        )

    async def stop_calculation_execution(
        self,
        request: AthenaStopCalculationExecutionRequest,
    ) -> AthenaStopCalculationExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_calculation_execution,
            request,
            AthenaStopCalculationExecutionResponse,
        )

    async def stop_query_execution(
        self,
        request: AthenaStopQueryExecutionRequest,
    ) -> AthenaStopQueryExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_query_execution,
            request,
            AthenaStopQueryExecutionResponse,
        )

    async def terminate_session(
        self,
        request: AthenaTerminateSessionRequest,
    ) -> AthenaTerminateSessionResponse:
        client = self._require_client()
        return await self._execute(
            client.terminate_session,
            request,
            AthenaTerminateSessionResponse,
        )

    async def update_data_catalog(
        self,
        request: AthenaUpdateDataCatalogRequest,
    ) -> AthenaUpdateDataCatalogResponse:
        client = self._require_client()
        return await self._execute(
            client.update_data_catalog,
            request,
            AthenaUpdateDataCatalogResponse,
        )

    async def update_named_query(
        self,
        request: AthenaUpdateNamedQueryRequest,
    ) -> AthenaUpdateNamedQueryResponse:
        client = self._require_client()
        return await self._execute(
            client.update_named_query,
            request,
            AthenaUpdateNamedQueryResponse,
        )

    async def batch_get_named_query(
        self,
        request: AthenaBatchGetNamedQueryRequest,
    ) -> AthenaBatchGetNamedQueryResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_named_query, request, AthenaBatchGetNamedQueryResponse)

    async def batch_get_prepared_statement(
        self,
        request: AthenaBatchGetPreparedStatementRequest,
    ) -> AthenaBatchGetPreparedStatementResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_prepared_statement, request, AthenaBatchGetPreparedStatementResponse)

    async def batch_get_query_execution(
        self,
        request: AthenaBatchGetQueryExecutionRequest,
    ) -> AthenaBatchGetQueryExecutionResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_query_execution, request, AthenaBatchGetQueryExecutionResponse)

    async def cancel_capacity_reservation(
        self,
        request: AthenaCancelCapacityReservationRequest,
    ) -> AthenaCancelCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.cancel_capacity_reservation, request, AthenaCancelCapacityReservationResponse)

    async def create_capacity_reservation(
        self,
        request: AthenaCreateCapacityReservationRequest,
    ) -> AthenaCreateCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_reservation, request, AthenaCreateCapacityReservationResponse)

    async def create_notebook(
        self,
        request: AthenaCreateNotebookRequest,
    ) -> AthenaCreateNotebookResponse:
        client = self._require_client()
        return await self._execute(client.create_notebook, request, AthenaCreateNotebookResponse)

    async def create_presigned_notebook_url(
        self,
        request: AthenaCreatePresignedNotebookUrlRequest,
    ) -> AthenaCreatePresignedNotebookUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_presigned_notebook_url, request, AthenaCreatePresignedNotebookUrlResponse)

    async def create_system_table_configuration(
        self,
        request: AthenaCreateSystemTableConfigurationRequest,
    ) -> AthenaCreateSystemTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_system_table_configuration, request, AthenaCreateSystemTableConfigurationResponse)

    async def create_work_group(
        self,
        request: AthenaCreateWorkGroupRequest,
    ) -> AthenaCreateWorkGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_work_group, request, AthenaCreateWorkGroupResponse)

    async def delete_capacity_reservation(
        self,
        request: AthenaDeleteCapacityReservationRequest,
    ) -> AthenaDeleteCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.delete_capacity_reservation, request, AthenaDeleteCapacityReservationResponse)

    async def delete_notebook(
        self,
        request: AthenaDeleteNotebookRequest,
    ) -> AthenaDeleteNotebookResponse:
        client = self._require_client()
        return await self._execute(client.delete_notebook, request, AthenaDeleteNotebookResponse)

    async def delete_system_table_configuration(
        self,
        request: AthenaDeleteSystemTableConfigurationRequest,
    ) -> AthenaDeleteSystemTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_system_table_configuration, request, AthenaDeleteSystemTableConfigurationResponse)

    async def delete_work_group(
        self,
        request: AthenaDeleteWorkGroupRequest,
    ) -> AthenaDeleteWorkGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_work_group, request, AthenaDeleteWorkGroupResponse)

    async def export_notebook(
        self,
        request: AthenaExportNotebookRequest,
    ) -> AthenaExportNotebookResponse:
        client = self._require_client()
        return await self._execute(client.export_notebook, request, AthenaExportNotebookResponse)

    async def get_capacity_assignment_configuration(
        self,
        request: AthenaGetCapacityAssignmentConfigurationRequest,
    ) -> AthenaGetCapacityAssignmentConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_assignment_configuration, request, AthenaGetCapacityAssignmentConfigurationResponse)

    async def get_capacity_reservation(
        self,
        request: AthenaGetCapacityReservationRequest,
    ) -> AthenaGetCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_reservation, request, AthenaGetCapacityReservationResponse)

    async def get_notebook_metadata(
        self,
        request: AthenaGetNotebookMetadataRequest,
    ) -> AthenaGetNotebookMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_notebook_metadata, request, AthenaGetNotebookMetadataResponse)

    async def get_query_runtime_statistics(
        self,
        request: AthenaGetQueryRuntimeStatisticsRequest,
    ) -> AthenaGetQueryRuntimeStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_query_runtime_statistics, request, AthenaGetQueryRuntimeStatisticsResponse)

    async def get_resource_dashboard(
        self,
        request: AthenaGetResourceDashboardRequest,
    ) -> AthenaGetResourceDashboardResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_dashboard, request, AthenaGetResourceDashboardResponse)

    async def get_session_endpoint(
        self,
        request: AthenaGetSessionEndpointRequest,
    ) -> AthenaGetSessionEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_session_endpoint, request, AthenaGetSessionEndpointResponse)

    async def get_system_table_configuration(
        self,
        request: AthenaGetSystemTableConfigurationRequest,
    ) -> AthenaGetSystemTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_system_table_configuration, request, AthenaGetSystemTableConfigurationResponse)

    async def get_table_metadata(
        self,
        request: AthenaGetTableMetadataRequest,
    ) -> AthenaGetTableMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_table_metadata, request, AthenaGetTableMetadataResponse)

    async def get_work_group(
        self,
        request: AthenaGetWorkGroupRequest,
    ) -> AthenaGetWorkGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_work_group, request, AthenaGetWorkGroupResponse)

    async def import_notebook(
        self,
        request: AthenaImportNotebookRequest,
    ) -> AthenaImportNotebookResponse:
        client = self._require_client()
        return await self._execute(client.import_notebook, request, AthenaImportNotebookResponse)

    async def list_application_dpu_sizes(
        self,
        request: AthenaListApplicationDPUSizesRequest | None = None,
    ) -> AthenaListApplicationDPUSizesResponse:
        client = self._require_client()
        return await self._execute(client.list_application_dpu_sizes, request, AthenaListApplicationDPUSizesResponse)

    async def list_calculation_executions(
        self,
        request: AthenaListCalculationExecutionsRequest,
    ) -> AthenaListCalculationExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_calculation_executions, request, AthenaListCalculationExecutionsResponse)

    async def list_capacity_reservations(
        self,
        request: AthenaListCapacityReservationsRequest | None = None,
    ) -> AthenaListCapacityReservationsResponse:
        client = self._require_client()
        return await self._execute(client.list_capacity_reservations, request, AthenaListCapacityReservationsResponse)

    async def list_engine_versions(
        self,
        request: AthenaListEngineVersionsRequest | None = None,
    ) -> AthenaListEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_engine_versions, request, AthenaListEngineVersionsResponse)

    async def list_executors(
        self,
        request: AthenaListExecutorsRequest,
    ) -> AthenaListExecutorsResponse:
        client = self._require_client()
        return await self._execute(client.list_executors, request, AthenaListExecutorsResponse)

    async def list_notebook_metadata(
        self,
        request: AthenaListNotebookMetadataRequest,
    ) -> AthenaListNotebookMetadataResponse:
        client = self._require_client()
        return await self._execute(client.list_notebook_metadata, request, AthenaListNotebookMetadataResponse)

    async def list_notebook_sessions(
        self,
        request: AthenaListNotebookSessionsRequest,
    ) -> AthenaListNotebookSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_notebook_sessions, request, AthenaListNotebookSessionsResponse)

    async def list_system_table_statuses(
        self,
        request: AthenaListSystemTableStatusesRequest | None = None,
    ) -> AthenaListSystemTableStatusesResponse:
        client = self._require_client()
        return await self._execute(client.list_system_table_statuses, request, AthenaListSystemTableStatusesResponse)

    async def list_system_table_statuses_paginated(
        self,
        request: AthenaListSystemTableStatusesRequest | None = None,
    ) -> list[AthenaListSystemTableStatusesResponse]:
        return await self._paginate('list_system_table_statuses', request, AthenaListSystemTableStatusesResponse)

    async def list_table_metadata(
        self,
        request: AthenaListTableMetadataRequest,
    ) -> AthenaListTableMetadataResponse:
        client = self._require_client()
        return await self._execute(client.list_table_metadata, request, AthenaListTableMetadataResponse)

    async def list_table_metadata_paginated(
        self,
        request: AthenaListTableMetadataRequest,
    ) -> list[AthenaListTableMetadataResponse]:
        return await self._paginate('list_table_metadata', request, AthenaListTableMetadataResponse)

    async def list_tags_for_resource(
        self,
        request: AthenaListTagsForResourceRequest,
    ) -> AthenaListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AthenaListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: AthenaListTagsForResourceRequest,
    ) -> list[AthenaListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, AthenaListTagsForResourceResponse)

    async def list_work_groups(
        self,
        request: AthenaListWorkGroupsRequest | None = None,
    ) -> AthenaListWorkGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_work_groups, request, AthenaListWorkGroupsResponse)

    async def put_capacity_assignment_configuration(
        self,
        request: AthenaPutCapacityAssignmentConfigurationRequest,
    ) -> AthenaPutCapacityAssignmentConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_capacity_assignment_configuration, request, AthenaPutCapacityAssignmentConfigurationResponse)

    async def tag_resource(
        self,
        request: AthenaTagResourceRequest,
    ) -> AthenaTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AthenaTagResourceResponse)

    async def untag_resource(
        self,
        request: AthenaUntagResourceRequest,
    ) -> AthenaUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AthenaUntagResourceResponse)

    async def update_capacity_reservation(
        self,
        request: AthenaUpdateCapacityReservationRequest,
    ) -> AthenaUpdateCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.update_capacity_reservation, request, AthenaUpdateCapacityReservationResponse)

    async def update_notebook(
        self,
        request: AthenaUpdateNotebookRequest,
    ) -> AthenaUpdateNotebookResponse:
        client = self._require_client()
        return await self._execute(client.update_notebook, request, AthenaUpdateNotebookResponse)

    async def update_notebook_metadata(
        self,
        request: AthenaUpdateNotebookMetadataRequest,
    ) -> AthenaUpdateNotebookMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_notebook_metadata, request, AthenaUpdateNotebookMetadataResponse)

    async def update_prepared_statement(
        self,
        request: AthenaUpdatePreparedStatementRequest,
    ) -> AthenaUpdatePreparedStatementResponse:
        client = self._require_client()
        return await self._execute(client.update_prepared_statement, request, AthenaUpdatePreparedStatementResponse)

    async def update_system_table_configuration(
        self,
        request: AthenaUpdateSystemTableConfigurationRequest,
    ) -> AthenaUpdateSystemTableConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_system_table_configuration, request, AthenaUpdateSystemTableConfigurationResponse)

    async def update_work_group(
        self,
        request: AthenaUpdateWorkGroupRequest,
    ) -> AthenaUpdateWorkGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_work_group, request, AthenaUpdateWorkGroupResponse)

