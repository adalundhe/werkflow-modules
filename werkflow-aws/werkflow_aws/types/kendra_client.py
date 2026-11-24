from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class KendraClient(ABC):

    @abstractmethod
    def associate_entities_to_experience(
        self,
        *,
        Id: str,
        IndexId: str,
        EntityList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_personas_to_entities(
        self,
        *,
        Id: str,
        IndexId: str,
        Personas: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_document(
        self,
        *,
        IndexId: str,
        DocumentIdList: list[str],
        DataSourceSyncJobMetricTarget: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_featured_results_set(
        self,
        *,
        IndexId: str,
        FeaturedResultsSetIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_document_status(
        self,
        *,
        IndexId: str,
        DocumentInfoList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_document(
        self,
        *,
        IndexId: str,
        Documents: list[dict[str, Any]],
        RoleArn: str | None = None,
        CustomDocumentEnrichmentConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def clear_query_suggestions(
        self,
        *,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_control_configuration(
        self,
        *,
        IndexId: str,
        Name: str,
        Description: str | None = None,
        AccessControlList: list[dict[str, Any]] | None = None,
        HierarchicalAccessControlList: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_source(
        self,
        *,
        Name: str,
        IndexId: str,
        Type: str,
        Configuration: dict[str, Any] | None = None,
        VpcConfiguration: dict[str, Any] | None = None,
        Description: str | None = None,
        Schedule: str | None = None,
        RoleArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        LanguageCode: str | None = None,
        CustomDocumentEnrichmentConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_experience(
        self,
        *,
        Name: str,
        IndexId: str,
        RoleArn: str | None = None,
        Configuration: dict[str, Any] | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_faq(
        self,
        *,
        IndexId: str,
        Name: str,
        S3Path: dict[str, Any],
        RoleArn: str,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        FileFormat: str | None = None,
        ClientToken: str | None = None,
        LanguageCode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_featured_results_set(
        self,
        *,
        IndexId: str,
        FeaturedResultsSetName: str,
        Description: str | None = None,
        ClientToken: str | None = None,
        Status: str | None = None,
        QueryTexts: list[str] | None = None,
        FeaturedDocuments: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_index(
        self,
        *,
        Name: str,
        RoleArn: str,
        Edition: str | None = None,
        ServerSideEncryptionConfiguration: dict[str, Any] | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        UserTokenConfigurations: list[dict[str, Any]] | None = None,
        UserContextPolicy: str | None = None,
        UserGroupResolutionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_query_suggestions_block_list(
        self,
        *,
        IndexId: str,
        Name: str,
        SourceS3Path: dict[str, Any],
        RoleArn: str,
        Description: str | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_thesaurus(
        self,
        *,
        IndexId: str,
        Name: str,
        RoleArn: str,
        SourceS3Path: dict[str, Any],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_control_configuration(
        self,
        *,
        IndexId: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_source(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_experience(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_faq(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_index(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_principal_mapping(
        self,
        *,
        IndexId: str,
        GroupId: str,
        DataSourceId: str | None = None,
        OrderingId: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_query_suggestions_block_list(
        self,
        *,
        IndexId: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_thesaurus(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_access_control_configuration(
        self,
        *,
        IndexId: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_source(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_experience(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_faq(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_featured_results_set(
        self,
        *,
        IndexId: str,
        FeaturedResultsSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_index(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_principal_mapping(
        self,
        *,
        IndexId: str,
        GroupId: str,
        DataSourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_query_suggestions_block_list(
        self,
        *,
        IndexId: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_query_suggestions_config(
        self,
        *,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_thesaurus(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_entities_from_experience(
        self,
        *,
        Id: str,
        IndexId: str,
        EntityList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_personas_from_entities(
        self,
        *,
        Id: str,
        IndexId: str,
        EntityIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_suggestions(
        self,
        *,
        IndexId: str,
        QueryText: str,
        MaxSuggestionsCount: int | None = None,
        SuggestionTypes: list[str] | None = None,
        AttributeSuggestionsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_snapshots(
        self,
        *,
        IndexId: str,
        Interval: str,
        MetricType: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_control_configurations(
        self,
        *,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_source_sync_jobs(
        self,
        *,
        Id: str,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StartTimeFilter: dict[str, Any] | None = None,
        StatusFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sources(
        self,
        *,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entity_personas(
        self,
        *,
        Id: str,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experience_entities(
        self,
        *,
        Id: str,
        IndexId: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experiences(
        self,
        *,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_faqs(
        self,
        *,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_featured_results_sets(
        self,
        *,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups_older_than_ordering_id(
        self,
        *,
        IndexId: str,
        OrderingId: int,
        DataSourceId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_indices(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_query_suggestions_block_lists(
        self,
        *,
        IndexId: str,
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
    def list_thesauri(
        self,
        *,
        IndexId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_principal_mapping(
        self,
        *,
        IndexId: str,
        GroupId: str,
        GroupMembers: dict[str, Any],
        DataSourceId: str | None = None,
        OrderingId: int | None = None,
        RoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query(
        self,
        *,
        IndexId: str,
        QueryText: str | None = None,
        AttributeFilter: dict[str, Any] | None = None,
        Facets: list[dict[str, Any]] | None = None,
        RequestedDocumentAttributes: list[str] | None = None,
        QueryResultTypeFilter: str | None = None,
        DocumentRelevanceOverrideConfigurations: list[dict[str, Any]] | None = None,
        PageNumber: int | None = None,
        PageSize: int | None = None,
        SortingConfiguration: dict[str, Any] | None = None,
        SortingConfigurations: list[dict[str, Any]] | None = None,
        UserContext: dict[str, Any] | None = None,
        VisitorId: str | None = None,
        SpellCorrectionConfiguration: dict[str, Any] | None = None,
        CollapseConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retrieve(
        self,
        *,
        IndexId: str,
        QueryText: str,
        AttributeFilter: dict[str, Any] | None = None,
        RequestedDocumentAttributes: list[str] | None = None,
        DocumentRelevanceOverrideConfigurations: list[dict[str, Any]] | None = None,
        PageNumber: int | None = None,
        PageSize: int | None = None,
        UserContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_source_sync_job(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_data_source_sync_job(
        self,
        *,
        Id: str,
        IndexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_feedback(
        self,
        *,
        IndexId: str,
        QueryId: str,
        ClickFeedbackItems: list[dict[str, Any]] | None = None,
        RelevanceFeedbackItems: list[dict[str, Any]] | None = None,
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
    def update_access_control_configuration(
        self,
        *,
        IndexId: str,
        Id: str,
        Name: str | None = None,
        Description: str | None = None,
        AccessControlList: list[dict[str, Any]] | None = None,
        HierarchicalAccessControlList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source(
        self,
        *,
        Id: str,
        IndexId: str,
        Name: str | None = None,
        Configuration: dict[str, Any] | None = None,
        VpcConfiguration: dict[str, Any] | None = None,
        Description: str | None = None,
        Schedule: str | None = None,
        RoleArn: str | None = None,
        LanguageCode: str | None = None,
        CustomDocumentEnrichmentConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_experience(
        self,
        *,
        Id: str,
        IndexId: str,
        Name: str | None = None,
        RoleArn: str | None = None,
        Configuration: dict[str, Any] | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_featured_results_set(
        self,
        *,
        IndexId: str,
        FeaturedResultsSetId: str,
        FeaturedResultsSetName: str | None = None,
        Description: str | None = None,
        Status: str | None = None,
        QueryTexts: list[str] | None = None,
        FeaturedDocuments: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_index(
        self,
        *,
        Id: str,
        Name: str | None = None,
        RoleArn: str | None = None,
        Description: str | None = None,
        DocumentMetadataConfigurationUpdates: list[dict[str, Any]] | None = None,
        CapacityUnits: dict[str, Any] | None = None,
        UserTokenConfigurations: list[dict[str, Any]] | None = None,
        UserContextPolicy: str | None = None,
        UserGroupResolutionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_query_suggestions_block_list(
        self,
        *,
        IndexId: str,
        Id: str,
        Name: str | None = None,
        Description: str | None = None,
        SourceS3Path: dict[str, Any] | None = None,
        RoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_query_suggestions_config(
        self,
        *,
        IndexId: str,
        Mode: str | None = None,
        QueryLogLookBackWindowInDays: int | None = None,
        IncludeQueriesWithoutUserInformation: bool | None = None,
        MinimumNumberOfQueryingUsers: int | None = None,
        MinimumQueryCount: int | None = None,
        AttributeSuggestionsConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_thesaurus(
        self,
        *,
        Id: str,
        IndexId: str,
        Name: str | None = None,
        Description: str | None = None,
        RoleArn: str | None = None,
        SourceS3Path: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
