from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class AthenaClient(ABC):

    @abstractmethod
    def create_data_catalog(
        self,
        *,
        Name: str,
        Type: str,
        Description: str | None = None,
        Parameters: dict[str, str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_named_query(
        self,
        *,
        Name: str,
        Database: str,
        QueryString: str,
        Description: str | None = None,
        ClientRequestToken: str | None = None,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_prepared_statement(
        self,
        *,
        StatementName: str,
        WorkGroup: str,
        QueryStatement: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_catalog(
        self,
        *,
        Name: str,
        DeleteCatalogOnly: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_named_query(
        self,
        *,
        NamedQueryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_prepared_statement(
        self,
        *,
        StatementName: str,
        WorkGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calculation_execution(
        self,
        *,
        CalculationExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calculation_execution_code(
        self,
        *,
        CalculationExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calculation_execution_status(
        self,
        *,
        CalculationExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_catalog(
        self,
        *,
        Name: str,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_database(
        self,
        *,
        CatalogName: str,
        DatabaseName: str,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_named_query(
        self,
        *,
        NamedQueryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_prepared_statement(
        self,
        *,
        StatementName: str,
        WorkGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_execution(
        self,
        *,
        QueryExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_results(
        self,
        *,
        QueryExecutionId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        QueryResultType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_status(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_catalogs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_databases(
        self,
        *,
        CatalogName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None,
        AttributesToGet: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_named_queries(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_prepared_statements(
        self,
        *,
        WorkGroup: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_query_executions(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sessions(
        self,
        *,
        WorkGroup: str,
        StateFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_calculation_execution(
        self,
        *,
        SessionId: str,
        Description: str | None = None,
        CalculationConfiguration: dict[str, Any] | None = None,
        CodeBlock: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_query_execution(
        self,
        *,
        QueryString: str,
        ClientRequestToken: str | None = None,
        QueryExecutionContext: dict[str, Any] | None = None,
        ResultConfiguration: dict[str, Any] | None = None,
        WorkGroup: str | None = None,
        ExecutionParameters: list[str] | None = None,
        ResultReuseConfiguration: dict[str, Any] | None = None,
        EngineConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_session(
        self,
        *,
        WorkGroup: str,
        EngineConfiguration: dict[str, Any],
        Description: str | None = None,
        ExecutionRole: str | None = None,
        MonitoringConfiguration: dict[str, Any] | None = None,
        NotebookVersion: str | None = None,
        SessionIdleTimeoutInMinutes: int | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CopyWorkGroupTags: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_calculation_execution(
        self,
        *,
        CalculationExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_query_execution(
        self,
        *,
        QueryExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_session(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_catalog(
        self,
        *,
        Name: str,
        Type: str,
        Description: str | None = None,
        Parameters: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_named_query(
        self,
        *,
        NamedQueryId: str,
        Name: str,
        QueryString: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_named_query(
        self,
        *,
        NamedQueryIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_prepared_statement(
        self,
        *,
        PreparedStatementNames: list[str],
        WorkGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_query_execution(
        self,
        *,
        QueryExecutionIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_capacity_reservation(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_reservation(
        self,
        *,
        TargetDpus: int,
        Name: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_notebook(
        self,
        *,
        WorkGroup: str,
        Name: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_presigned_notebook_url(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_system_table_configuration(
        self,
        *,
        TableName: str,
        ClientRequestToken: str | None = None,
        KmsKeyArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_work_group(
        self,
        *,
        Name: str,
        Configuration: dict[str, Any] | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_capacity_reservation(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notebook(
        self,
        *,
        NotebookId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_system_table_configuration(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_work_group(
        self,
        *,
        WorkGroup: str,
        RecursiveDeleteOption: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_notebook(
        self,
        *,
        NotebookId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_assignment_configuration(
        self,
        *,
        CapacityReservationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_reservation(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_notebook_metadata(
        self,
        *,
        NotebookId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_runtime_statistics(
        self,
        *,
        QueryExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_dashboard(
        self,
        *,
        ResourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_endpoint(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_system_table_configuration(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_table_metadata(
        self,
        *,
        CatalogName: str,
        DatabaseName: str,
        TableName: str,
        WorkGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_work_group(
        self,
        *,
        WorkGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_notebook(
        self,
        *,
        WorkGroup: str,
        Name: str,
        Type: str,
        Payload: str | None = None,
        NotebookS3LocationUri: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_application_dpu_sizes(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_calculation_executions(
        self,
        *,
        SessionId: str,
        StateFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_capacity_reservations(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_engine_versions(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_executors(
        self,
        *,
        SessionId: str,
        ExecutorStateFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebook_metadata(
        self,
        *,
        WorkGroup: str,
        Filters: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebook_sessions(
        self,
        *,
        NotebookId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_system_table_statuses(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_table_metadata(
        self,
        *,
        CatalogName: str,
        DatabaseName: str,
        Expression: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None,
        AttributesToGet: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_work_groups(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_capacity_assignment_configuration(
        self,
        *,
        CapacityReservationName: str,
        CapacityAssignments: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_capacity_reservation(
        self,
        *,
        TargetDpus: int,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notebook(
        self,
        *,
        NotebookId: str,
        Payload: str,
        Type: str,
        SessionId: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notebook_metadata(
        self,
        *,
        NotebookId: str,
        Name: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_prepared_statement(
        self,
        *,
        StatementName: str,
        WorkGroup: str,
        QueryStatement: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_system_table_configuration(
        self,
        *,
        TableName: str,
        KmsKeyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_work_group(
        self,
        *,
        WorkGroup: str,
        Description: str | None = None,
        ConfigurationUpdates: dict[str, Any] | None = None,
        State: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
