from abc import ABC, abstractmethod
from botocore.paginate import Paginator
from typing import Literal, Any


AthenaQueryResultType = Literal['DATA_MANIFEST', 'DATA_ROWS']

AthenaDataCatalogType = Literal[
    'LAMBDA',
    'GLUE',
    'HIVE',
    'FEDERATED',
]

AthenaClientTag = dict[
    Literal['Key', 'Value'],
    str,
]

AthenaCalculationExecution = dict[
    Literal["CodeBlock"],
    str,
]

AthenaResultReuseConfiguration = dict[
    Literal["ResultReuseByAgeConfiguration"],
    dict[
        Literal["Enabled", "MaxAgeInMinutes"],
        bool | int
    ]
]

AthenaQueryExecutionContext = dict[
    Literal["Database", "Catalog"],
    str,
]

AthenaEncryptionOption = Literal['SSE_S3','SSE_KMS','CSE_KMS']

AthenaAclConfiguration = dict[
    Literal["S3AclOption"],
    str
]

AthenaEncryptionConfiguration = dict[
    Literal["EncryptionOption", "KmsKey"],
    AthenaEncryptionOption | str
]

AthenaResultConfiguration = dict[
    Literal[
        "OutputLocation",
        "EncryptionConfiguration",
        "ExpectedBucketOwner",
        "AclConfiguration",
    ],
    str | AthenaAclConfiguration | AthenaEncryptionConfiguration
]

AthenaSessionStateFilter = Literal[
    'CREATING',
    'CREATED',
    'IDLE',
    'BUSY',
    'TERMINATING',
    'TERMINATED',
    'DEGRADED',
    'FAILED',
]

AthenaEngineConfiguration = dict[
    Literal[
        "CoordinatorDpuSize",
        "MaxConcurrentDpus",
        "DefaultExecutorDpuSize",
        "AdditionalConfigs",
        "SparkProperties",
    ],
    int | dict[str, str]
]

class AthenaClient(ABC):

    @abstractmethod
    def create_data_catalog(
        self,
        Name: str = None,
        Type: AthenaDataCatalogType = None,
        Description: str = None,
        Parameters: dict[str, str] | None = None,
        Tags: list[AthenaClientTag] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_named_query(
        self,
        Name: str = None,
        Description: str = None,
        Database: str = None,
        QueryString: str = None,
        ClientRequestToken: str = None,
        WorkGroup: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_prepared_statement(
        self,
        StatementName: str = None,
        WorkGroup: str = None,
        QueryStatement: str = None,
        Description: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calculation_execution(
        self,
        CalculationExecutionId: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calculation_execution_code(
        self,
        CalculationExecutionId: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calculation_execution_status(
        self,
        CalculationExecutionId: str = None,

    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_catalog(
        self,
        Name: str = None,
        WorkGroup: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_database(
        self,
        CatalogName: str = None,
        DatabaseName: str = None,
        WorkGroup: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_named_query(
        self,
        NamedQueryId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_prepared_statement(
        self,
        StatementName: str = None,
        WorkGroup: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_execution(
        self,
        QueryExecutionId: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_results(
        self,
        QueryExecutionId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        QueryResultType: AthenaQueryResultType = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_named_queries(
        self,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def list_query_executions(
        self,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def list_sessions(
        self,
        WorkGroup='string',
        StateFilter: AthenaSessionStateFilter = None,
        MaxResults=123,
        NextToken='string'
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def list_prepared_statements(
        self,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        WorkGroup: str | None = None
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def list_databases(
        self,
        CatalogName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        WorkGroup: str = None
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def list_data_catalogs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        WorkGroup: str = None,
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def get_session(
        self,
        SessionId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_status(
        self,
        SessionId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_calculation_execution(
        self,
        SessionId: str = None,
        Description: str = None,
        CalculationConfiguration: AthenaCalculationExecution = None,
        CodeBlock: str = None,
        ClientRequestToken: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_query_execution(
        self,
        QueryString: str = None,
        ClientRequestToken: str = None,
        QueryExecutionContext: AthenaQueryExecutionContext = None,
        ResultConfiguration: AthenaResultConfiguration = None,
        WorkGroup: str = None,
        ExecutionParameters: list[str] = None,
        ResultReuseConfiguration: AthenaResultReuseConfiguration = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_session(
        self,
        Description: str = None,
        WorkGroup: str = None,
        EngineConfiguration: AthenaEngineConfiguration = None,
        NotebookVersion: str = None,
        SessionIdleTimeoutInMinutes: int = None,
        ClientRequestToken: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_calculation_execution(
        self,
        CalculationExecutionId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_query_execution(
        self,
        QueryExecutionId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_session(
        self,
        SessionId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_catalog(
        self,
        Name: str = None,
        Type: AthenaDataCatalogType = None,
        Description: str = None,
        Parameters: dict[str, str] = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_named_query(
        self,
        NamedQueryId: str = None,
        Name: str = None,
        Description: str = None,
        QueryString: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_named_query(
        self,
        NamedQueryId: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_prepared_statement(
        self,
        StatementName: str = None,
        WorkGroup: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_catalog(
        self,
        Name: str = None,
        DeleteCatalogOnly: bool = False
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(
        self,
        Operation: str,
    ) -> Paginator:
        pass

    @abstractmethod
    def close(self):
        pass