from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class LakeFormationClient(ABC):

    @abstractmethod
    def add_lf_tags_to_resource(
        self,
        *,
        Resource: dict[str, Any],
        LFTags: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assume_decorated_role_with_saml(
        self,
        *,
        SAMLAssertion: str,
        RoleArn: str,
        PrincipalArn: str,
        DurationSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_rls_policy(
        self,
        *,
        Name: str,
        Resource: dict[str, Any],
        Principal: dict[str, Any] | None = None,
        Condition: dict[str, Any] | None = None,
        SetDefault: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_grant_permissions(
        self,
        *,
        Entries: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_revoke_permissions(
        self,
        *,
        Entries: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_transaction(
        self,
        *,
        TransactionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def commit_transaction(
        self,
        *,
        TransactionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_cells_filter(
        self,
        *,
        TableData: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lf_tag(
        self,
        *,
        TagKey: str,
        TagValues: list[str],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lf_tag_expression(
        self,
        *,
        Name: str,
        Expression: list[dict[str, Any]],
        Description: str | None = None,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lake_formation_identity_center_configuration(
        self,
        *,
        CatalogId: str | None = None,
        InstanceArn: str | None = None,
        ExternalFiltering: dict[str, Any] | None = None,
        ShareRecipients: list[dict[str, Any]] | None = None,
        ServiceIntegrations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lake_formation_opt_in(
        self,
        *,
        Principal: dict[str, Any],
        Resource: dict[str, Any],
        Condition: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rls_policy(
        self,
        *,
        Name: str,
        AttachmentColumns: list[dict[str, Any]],
        FilterExpression: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_cells_filter(
        self,
        *,
        TableCatalogId: str | None = None,
        DatabaseName: str | None = None,
        TableName: str | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lf_tag(
        self,
        *,
        TagKey: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lf_tag_expression(
        self,
        *,
        Name: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lake_formation_identity_center_configuration(
        self,
        *,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lake_formation_opt_in(
        self,
        *,
        Principal: dict[str, Any],
        Resource: dict[str, Any],
        Condition: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_objects_on_cancel(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        TransactionId: str,
        Objects: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rls_policy(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lake_formation_identity_center_configuration(
        self,
        *,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transaction(
        self,
        *,
        TransactionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_rls_policy(
        self,
        *,
        Name: str,
        Resource: dict[str, Any],
        Principal: dict[str, Any] | None = None,
        Condition: dict[str, Any] | None = None,
        RemoveDefault: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def extend_transaction(
        self,
        *,
        TransactionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_cells_filter(
        self,
        *,
        TableCatalogId: str,
        DatabaseName: str,
        TableName: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_lake_principal(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_lake_settings(
        self,
        *,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_effective_permissions_for_path(
        self,
        *,
        ResourceArn: str,
        CatalogId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_glue_function_session_context(
        self,
        *,
        UserDefinedFunctionArns: list[str],
        DurationSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lf_tag(
        self,
        *,
        TagKey: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lf_tag_expression(
        self,
        *,
        Name: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_state(
        self,
        *,
        QueryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_statistics(
        self,
        *,
        QueryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rls_policy(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_lf_tags(
        self,
        *,
        Resource: dict[str, Any],
        CatalogId: str | None = None,
        ShowAssignedLFTags: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_table_objects(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str | None = None,
        TransactionId: str | None = None,
        QueryAsOfTime: datetime.datetime | str | None = None,
        PartitionPredicate: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_temporary_data_location_credentials(
        self,
        *,
        DurationSeconds: int | None = None,
        AuditContext: dict[str, Any] | None = None,
        DataLocations: list[str] | None = None,
        CredentialsScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_temporary_glue_function_credentials(
        self,
        *,
        UserDefinedFunctionArn: str,
        AuditContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_temporary_glue_partition_credentials(
        self,
        *,
        TableArn: str,
        Partition: dict[str, Any],
        Permissions: list[str] | None = None,
        DurationSeconds: int | None = None,
        AuditContext: dict[str, Any] | None = None,
        SupportedPermissionTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_temporary_glue_table_credentials(
        self,
        *,
        TableArn: str,
        Permissions: list[str] | None = None,
        DurationSeconds: int | None = None,
        AuditContext: dict[str, Any] | None = None,
        SupportedPermissionTypes: list[str] | None = None,
        S3Path: str | None = None,
        QuerySessionContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_work_unit_results(
        self,
        *,
        QueryId: str,
        WorkUnitId: int,
        WorkUnitToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_work_units(
        self,
        *,
        QueryId: str,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def grant_permissions(
        self,
        *,
        Principal: dict[str, Any],
        Resource: dict[str, Any],
        Permissions: list[str],
        CatalogId: str | None = None,
        Condition: dict[str, Any] | None = None,
        PermissionsWithGrantOption: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_cells_filter(
        self,
        *,
        Table: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lf_tag_expressions(
        self,
        *,
        CatalogId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lf_tags(
        self,
        *,
        CatalogId: str | None = None,
        ResourceShareType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lake_formation_opt_ins(
        self,
        *,
        Principal: dict[str, Any] | None = None,
        Resource: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_permissions(
        self,
        *,
        CatalogId: str | None = None,
        Principal: dict[str, Any] | None = None,
        ResourceType: str | None = None,
        Resource: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IncludeRelated: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rls_policies(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rls_policy_attachments(
        self,
        *,
        Resource: dict[str, Any] | None = None,
        Principal: dict[str, Any] | None = None,
        PolicyName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resources(
        self,
        *,
        FilterConditionList: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_table_storage_optimizers(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str | None = None,
        StorageOptimizerType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_transactions(
        self,
        *,
        CatalogId: str | None = None,
        StatusFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_lake_settings(
        self,
        *,
        DataLakeSettings: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_resource(
        self,
        *,
        ResourceArn: str,
        UseServiceLinkedRole: bool | None = None,
        RoleArn: str | None = None,
        WithFederation: bool | None = None,
        HybridAccessEnabled: bool | None = None,
        WithPrivilegedAccess: bool | None = None,
        ExpectedResourceOwnerAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_lf_tags_from_resource(
        self,
        *,
        Resource: dict[str, Any],
        LFTags: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_permissions(
        self,
        *,
        Principal: dict[str, Any],
        Resource: dict[str, Any],
        Permissions: list[str],
        CatalogId: str | None = None,
        Condition: dict[str, Any] | None = None,
        PermissionsWithGrantOption: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_databases_by_lf_tags(
        self,
        *,
        Expression: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_tables_by_lf_tags(
        self,
        *,
        Expression: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_query_planning(
        self,
        *,
        QueryPlanningContext: dict[str, Any],
        QueryString: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_transaction(
        self,
        *,
        TransactionType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_cells_filter(
        self,
        *,
        TableData: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_lf_tag(
        self,
        *,
        TagKey: str,
        CatalogId: str | None = None,
        TagValuesToDelete: list[str] | None = None,
        TagValuesToAdd: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_lf_tag_expression(
        self,
        *,
        Name: str,
        Expression: list[dict[str, Any]],
        Description: str | None = None,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_lake_formation_identity_center_configuration(
        self,
        *,
        CatalogId: str | None = None,
        ShareRecipients: list[dict[str, Any]] | None = None,
        ServiceIntegrations: list[dict[str, Any]] | None = None,
        ApplicationStatus: str | None = None,
        ExternalFiltering: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rls_policy(
        self,
        *,
        Name: str,
        FilterExpression: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource(
        self,
        *,
        RoleArn: str,
        ResourceArn: str,
        WithFederation: bool | None = None,
        HybridAccessEnabled: bool | None = None,
        ExpectedResourceOwnerAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table_objects(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        WriteOperations: list[dict[str, Any]],
        CatalogId: str | None = None,
        TransactionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table_storage_optimizer(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        StorageOptimizerConfig: dict[str, dict[str, str]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
