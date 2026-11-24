from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class TimestreamWriteClient(ABC):

    @abstractmethod
    def create_batch_load_task(
        self,
        *,
        DataSourceConfiguration: dict[str, Any],
        ReportConfiguration: dict[str, Any],
        TargetDatabaseName: str,
        TargetTableName: str,
        ClientToken: str | None = None,
        DataModelConfiguration: dict[str, Any] | None = None,
        RecordVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_database(
        self,
        *,
        DatabaseName: str,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        RetentionProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        MagneticStoreWriteProperties: dict[str, Any] | None = None,
        Schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_database(
        self,
        *,
        DatabaseName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_batch_load_task(
        self,
        *,
        TaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_database(
        self,
        *,
        DatabaseName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoints(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_batch_load_tasks(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        TaskStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_databases(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tables(
        self,
        *,
        DatabaseName: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_batch_load_task(
        self,
        *,
        TaskId: str,
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
    def update_database(
        self,
        *,
        DatabaseName: str,
        KmsKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        RetentionProperties: dict[str, Any] | None = None,
        MagneticStoreWriteProperties: dict[str, Any] | None = None,
        Schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def write_records(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Records: list[dict[str, Any]],
        CommonAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
