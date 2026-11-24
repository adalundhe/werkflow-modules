from werkflow_aws.models.codecommit import (
    CodeCommitAssociateApprovalRuleTemplateWithRepositoryRequest,
    CodeCommitAssociateApprovalRuleTemplateWithRepositoryResponse,
    CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesRequest,
    CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesResponse,
    CodeCommitBatchDescribeMergeConflictsRequest,
    CodeCommitBatchDescribeMergeConflictsResponse,
    CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesRequest,
    CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesResponse,
    CodeCommitBatchGetCommitsRequest,
    CodeCommitBatchGetCommitsResponse,
    CodeCommitBatchGetRepositoriesRequest,
    CodeCommitBatchGetRepositoriesResponse,
    CodeCommitCreateApprovalRuleTemplateRequest,
    CodeCommitCreateApprovalRuleTemplateResponse,
    CodeCommitCreateBranchRequest,
    CodeCommitCreateBranchResponse,
    CodeCommitCreateCommitRequest,
    CodeCommitCreateCommitResponse,
    CodeCommitCreatePullRequestApprovalRuleRequest,
    CodeCommitCreatePullRequestApprovalRuleResponse,
    CodeCommitCreatePullRequestRequest,
    CodeCommitCreatePullRequestResponse,
    CodeCommitCreateRepositoryRequest,
    CodeCommitCreateRepositoryResponse,
    CodeCommitCreateUnreferencedMergeCommitRequest,
    CodeCommitCreateUnreferencedMergeCommitResponse,
    CodeCommitDeleteApprovalRuleTemplateRequest,
    CodeCommitDeleteApprovalRuleTemplateResponse,
    CodeCommitDeleteBranchRequest,
    CodeCommitDeleteBranchResponse,
    CodeCommitDeleteCommentContentRequest,
    CodeCommitDeleteCommentContentResponse,
    CodeCommitDeleteFileRequest,
    CodeCommitDeleteFileResponse,
    CodeCommitDeletePullRequestApprovalRuleRequest,
    CodeCommitDeletePullRequestApprovalRuleResponse,
    CodeCommitDeleteRepositoryRequest,
    CodeCommitDeleteRepositoryResponse,
    CodeCommitDescribeMergeConflictsRequest,
    CodeCommitDescribeMergeConflictsResponse,
    CodeCommitDescribePullRequestEventsRequest,
    CodeCommitDescribePullRequestEventsResponse,
    CodeCommitDisassociateApprovalRuleTemplateFromRepositoryRequest,
    CodeCommitDisassociateApprovalRuleTemplateFromRepositoryResponse,
    CodeCommitEvaluatePullRequestApprovalRulesRequest,
    CodeCommitEvaluatePullRequestApprovalRulesResponse,
    CodeCommitGetApprovalRuleTemplateRequest,
    CodeCommitGetApprovalRuleTemplateResponse,
    CodeCommitGetBlobDifferencesRequest,
    CodeCommitGetBlobDifferencesResponse,
    CodeCommitGetBlobRequest,
    CodeCommitGetBlobResponse,
    CodeCommitGetBranchRequest,
    CodeCommitGetBranchResponse,
    CodeCommitGetCommentReactionsRequest,
    CodeCommitGetCommentReactionsResponse,
    CodeCommitGetCommentRequest,
    CodeCommitGetCommentResponse,
    CodeCommitGetCommentsForComparedCommitRequest,
    CodeCommitGetCommentsForComparedCommitResponse,
    CodeCommitGetCommentsForPullRequestRequest,
    CodeCommitGetCommentsForPullRequestResponse,
    CodeCommitGetCommitRequest,
    CodeCommitGetCommitResponse,
    CodeCommitGetDifferencesRequest,
    CodeCommitGetDifferencesResponse,
    CodeCommitGetFileRequest,
    CodeCommitGetFileResponse,
    CodeCommitGetFolderRequest,
    CodeCommitGetFolderResponse,
    CodeCommitGetMergeCommitRequest,
    CodeCommitGetMergeCommitResponse,
    CodeCommitGetMergeConflictsRequest,
    CodeCommitGetMergeConflictsResponse,
    CodeCommitGetMergeOptionsRequest,
    CodeCommitGetMergeOptionsResponse,
    CodeCommitGetPullRequestApprovalStatesRequest,
    CodeCommitGetPullRequestApprovalStatesResponse,
    CodeCommitGetPullRequestOverrideStateRequest,
    CodeCommitGetPullRequestOverrideStateResponse,
    CodeCommitGetPullRequestRequest,
    CodeCommitGetPullRequestResponse,
    CodeCommitGetRepositoryRequest,
    CodeCommitGetRepositoryResponse,
    CodeCommitGetRepositoryTriggersRequest,
    CodeCommitGetRepositoryTriggersResponse,
    CodeCommitListApprovalRuleTemplatesRequest,
    CodeCommitListApprovalRuleTemplatesResponse,
    CodeCommitListAssociatedApprovalRuleTemplatesForRepositoryRequest,
    CodeCommitListAssociatedApprovalRuleTemplatesForRepositoryResponse,
    CodeCommitListBranchesRequest,
    CodeCommitListBranchesResponse,
    CodeCommitListFileCommitHistoryRequest,
    CodeCommitListFileCommitHistoryResponse,
    CodeCommitListPullRequestsRequest,
    CodeCommitListPullRequestsResponse,
    CodeCommitListRepositoriesForApprovalRuleTemplateRequest,
    CodeCommitListRepositoriesForApprovalRuleTemplateResponse,
    CodeCommitListRepositoriesRequest,
    CodeCommitListRepositoriesResponse,
    CodeCommitListTagsForResourceRequest,
    CodeCommitListTagsForResourceResponse,
    CodeCommitMergeBranchesByFastForwardRequest,
    CodeCommitMergeBranchesByFastForwardResponse,
    CodeCommitMergeBranchesBySquashRequest,
    CodeCommitMergeBranchesBySquashResponse,
    CodeCommitMergeBranchesByThreeWayRequest,
    CodeCommitMergeBranchesByThreeWayResponse,
    CodeCommitMergePullRequestByFastForwardRequest,
    CodeCommitMergePullRequestByFastForwardResponse,
    CodeCommitMergePullRequestBySquashRequest,
    CodeCommitMergePullRequestBySquashResponse,
    CodeCommitMergePullRequestByThreeWayRequest,
    CodeCommitMergePullRequestByThreeWayResponse,
    CodeCommitOverridePullRequestApprovalRulesRequest,
    CodeCommitOverridePullRequestApprovalRulesResponse,
    CodeCommitPostCommentForComparedCommitRequest,
    CodeCommitPostCommentForComparedCommitResponse,
    CodeCommitPostCommentForPullRequestRequest,
    CodeCommitPostCommentForPullRequestResponse,
    CodeCommitPostCommentReplyRequest,
    CodeCommitPostCommentReplyResponse,
    CodeCommitPutCommentReactionRequest,
    CodeCommitPutCommentReactionResponse,
    CodeCommitPutFileRequest,
    CodeCommitPutFileResponse,
    CodeCommitPutRepositoryTriggersRequest,
    CodeCommitPutRepositoryTriggersResponse,
    CodeCommitTagResourceRequest,
    CodeCommitTagResourceResponse,
    CodeCommitTestRepositoryTriggersRequest,
    CodeCommitTestRepositoryTriggersResponse,
    CodeCommitUntagResourceRequest,
    CodeCommitUntagResourceResponse,
    CodeCommitUpdateApprovalRuleTemplateContentRequest,
    CodeCommitUpdateApprovalRuleTemplateContentResponse,
    CodeCommitUpdateApprovalRuleTemplateDescriptionRequest,
    CodeCommitUpdateApprovalRuleTemplateDescriptionResponse,
    CodeCommitUpdateApprovalRuleTemplateNameRequest,
    CodeCommitUpdateApprovalRuleTemplateNameResponse,
    CodeCommitUpdateCommentRequest,
    CodeCommitUpdateCommentResponse,
    CodeCommitUpdateDefaultBranchRequest,
    CodeCommitUpdateDefaultBranchResponse,
    CodeCommitUpdatePullRequestApprovalRuleContentRequest,
    CodeCommitUpdatePullRequestApprovalRuleContentResponse,
    CodeCommitUpdatePullRequestApprovalStateRequest,
    CodeCommitUpdatePullRequestApprovalStateResponse,
    CodeCommitUpdatePullRequestDescriptionRequest,
    CodeCommitUpdatePullRequestDescriptionResponse,
    CodeCommitUpdatePullRequestStatusRequest,
    CodeCommitUpdatePullRequestStatusResponse,
    CodeCommitUpdatePullRequestTitleRequest,
    CodeCommitUpdatePullRequestTitleResponse,
    CodeCommitUpdateRepositoryDescriptionRequest,
    CodeCommitUpdateRepositoryDescriptionResponse,
    CodeCommitUpdateRepositoryEncryptionKeyRequest,
    CodeCommitUpdateRepositoryEncryptionKeyResponse,
    CodeCommitUpdateRepositoryNameRequest,
    CodeCommitUpdateRepositoryNameResponse,
)
from werkflow_aws.types.codecommit_client import CodeCommitClient
from .base import AWSBaseService


class AWSCodeCommit(AWSBaseService[CodeCommitClient]):
    service_name = 'codecommit'
    boto3_service_name = 'codecommit'

    def __init__(self) -> None:
        super().__init__(service_name='codecommit', boto3_service_name='codecommit')

    async def associate_approval_rule_template_with_repository(
        self,
        request: CodeCommitAssociateApprovalRuleTemplateWithRepositoryRequest,
    ) -> CodeCommitAssociateApprovalRuleTemplateWithRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.associate_approval_rule_template_with_repository, request, CodeCommitAssociateApprovalRuleTemplateWithRepositoryResponse)

    async def batch_associate_approval_rule_template_with_repositories(
        self,
        request: CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesRequest,
    ) -> CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_approval_rule_template_with_repositories, request, CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesResponse)

    async def batch_describe_merge_conflicts(
        self,
        request: CodeCommitBatchDescribeMergeConflictsRequest,
    ) -> CodeCommitBatchDescribeMergeConflictsResponse:
        client = self._require_client()
        return await self._execute(client.batch_describe_merge_conflicts, request, CodeCommitBatchDescribeMergeConflictsResponse)

    async def batch_disassociate_approval_rule_template_from_repositories(
        self,
        request: CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesRequest,
    ) -> CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_approval_rule_template_from_repositories, request, CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesResponse)

    async def batch_get_commits(
        self,
        request: CodeCommitBatchGetCommitsRequest,
    ) -> CodeCommitBatchGetCommitsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_commits, request, CodeCommitBatchGetCommitsResponse)

    async def batch_get_repositories(
        self,
        request: CodeCommitBatchGetRepositoriesRequest,
    ) -> CodeCommitBatchGetRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_repositories, request, CodeCommitBatchGetRepositoriesResponse)

    async def create_approval_rule_template(
        self,
        request: CodeCommitCreateApprovalRuleTemplateRequest,
    ) -> CodeCommitCreateApprovalRuleTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_approval_rule_template, request, CodeCommitCreateApprovalRuleTemplateResponse)

    async def create_branch(
        self,
        request: CodeCommitCreateBranchRequest,
    ) -> CodeCommitCreateBranchResponse:
        client = self._require_client()
        return await self._execute(client.create_branch, request, CodeCommitCreateBranchResponse)

    async def create_commit(
        self,
        request: CodeCommitCreateCommitRequest,
    ) -> CodeCommitCreateCommitResponse:
        client = self._require_client()
        return await self._execute(client.create_commit, request, CodeCommitCreateCommitResponse)

    async def create_pull_request(
        self,
        request: CodeCommitCreatePullRequestRequest,
    ) -> CodeCommitCreatePullRequestResponse:
        client = self._require_client()
        return await self._execute(client.create_pull_request, request, CodeCommitCreatePullRequestResponse)

    async def create_pull_request_approval_rule(
        self,
        request: CodeCommitCreatePullRequestApprovalRuleRequest,
    ) -> CodeCommitCreatePullRequestApprovalRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_pull_request_approval_rule, request, CodeCommitCreatePullRequestApprovalRuleResponse)

    async def create_repository(
        self,
        request: CodeCommitCreateRepositoryRequest,
    ) -> CodeCommitCreateRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.create_repository, request, CodeCommitCreateRepositoryResponse)

    async def create_unreferenced_merge_commit(
        self,
        request: CodeCommitCreateUnreferencedMergeCommitRequest,
    ) -> CodeCommitCreateUnreferencedMergeCommitResponse:
        client = self._require_client()
        return await self._execute(client.create_unreferenced_merge_commit, request, CodeCommitCreateUnreferencedMergeCommitResponse)

    async def delete_approval_rule_template(
        self,
        request: CodeCommitDeleteApprovalRuleTemplateRequest,
    ) -> CodeCommitDeleteApprovalRuleTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_approval_rule_template, request, CodeCommitDeleteApprovalRuleTemplateResponse)

    async def delete_branch(
        self,
        request: CodeCommitDeleteBranchRequest,
    ) -> CodeCommitDeleteBranchResponse:
        client = self._require_client()
        return await self._execute(client.delete_branch, request, CodeCommitDeleteBranchResponse)

    async def delete_comment_content(
        self,
        request: CodeCommitDeleteCommentContentRequest,
    ) -> CodeCommitDeleteCommentContentResponse:
        client = self._require_client()
        return await self._execute(client.delete_comment_content, request, CodeCommitDeleteCommentContentResponse)

    async def delete_file(
        self,
        request: CodeCommitDeleteFileRequest,
    ) -> CodeCommitDeleteFileResponse:
        client = self._require_client()
        return await self._execute(client.delete_file, request, CodeCommitDeleteFileResponse)

    async def delete_pull_request_approval_rule(
        self,
        request: CodeCommitDeletePullRequestApprovalRuleRequest,
    ) -> CodeCommitDeletePullRequestApprovalRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_pull_request_approval_rule, request, CodeCommitDeletePullRequestApprovalRuleResponse)

    async def delete_repository(
        self,
        request: CodeCommitDeleteRepositoryRequest,
    ) -> CodeCommitDeleteRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository, request, CodeCommitDeleteRepositoryResponse)

    async def describe_merge_conflicts(
        self,
        request: CodeCommitDescribeMergeConflictsRequest,
    ) -> CodeCommitDescribeMergeConflictsResponse:
        client = self._require_client()
        return await self._execute(client.describe_merge_conflicts, request, CodeCommitDescribeMergeConflictsResponse)

    async def describe_pull_request_events(
        self,
        request: CodeCommitDescribePullRequestEventsRequest,
    ) -> CodeCommitDescribePullRequestEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pull_request_events, request, CodeCommitDescribePullRequestEventsResponse)

    async def describe_pull_request_events_paginated(
        self,
        request: CodeCommitDescribePullRequestEventsRequest,
    ) -> list[CodeCommitDescribePullRequestEventsResponse]:
        return await self._paginate('describe_pull_request_events', request, CodeCommitDescribePullRequestEventsResponse)

    async def disassociate_approval_rule_template_from_repository(
        self,
        request: CodeCommitDisassociateApprovalRuleTemplateFromRepositoryRequest,
    ) -> CodeCommitDisassociateApprovalRuleTemplateFromRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_approval_rule_template_from_repository, request, CodeCommitDisassociateApprovalRuleTemplateFromRepositoryResponse)

    async def evaluate_pull_request_approval_rules(
        self,
        request: CodeCommitEvaluatePullRequestApprovalRulesRequest,
    ) -> CodeCommitEvaluatePullRequestApprovalRulesResponse:
        client = self._require_client()
        return await self._execute(client.evaluate_pull_request_approval_rules, request, CodeCommitEvaluatePullRequestApprovalRulesResponse)

    async def get_approval_rule_template(
        self,
        request: CodeCommitGetApprovalRuleTemplateRequest,
    ) -> CodeCommitGetApprovalRuleTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_approval_rule_template, request, CodeCommitGetApprovalRuleTemplateResponse)

    async def get_blob(
        self,
        request: CodeCommitGetBlobRequest,
    ) -> CodeCommitGetBlobResponse:
        client = self._require_client()
        return await self._execute(client.get_blob, request, CodeCommitGetBlobResponse)

    async def get_blob_differences(
        self,
        request: CodeCommitGetBlobDifferencesRequest,
    ) -> CodeCommitGetBlobDifferencesResponse:
        client = self._require_client()
        return await self._execute(client.get_blob_differences, request, CodeCommitGetBlobDifferencesResponse)

    async def get_blob_differences_paginated(
        self,
        request: CodeCommitGetBlobDifferencesRequest,
    ) -> list[CodeCommitGetBlobDifferencesResponse]:
        return await self._paginate('get_blob_differences', request, CodeCommitGetBlobDifferencesResponse)

    async def get_branch(
        self,
        request: CodeCommitGetBranchRequest | None = None,
    ) -> CodeCommitGetBranchResponse:
        client = self._require_client()
        return await self._execute(client.get_branch, request, CodeCommitGetBranchResponse)

    async def get_comment(
        self,
        request: CodeCommitGetCommentRequest,
    ) -> CodeCommitGetCommentResponse:
        client = self._require_client()
        return await self._execute(client.get_comment, request, CodeCommitGetCommentResponse)

    async def get_comment_reactions(
        self,
        request: CodeCommitGetCommentReactionsRequest,
    ) -> CodeCommitGetCommentReactionsResponse:
        client = self._require_client()
        return await self._execute(client.get_comment_reactions, request, CodeCommitGetCommentReactionsResponse)

    async def get_comments_for_compared_commit(
        self,
        request: CodeCommitGetCommentsForComparedCommitRequest,
    ) -> CodeCommitGetCommentsForComparedCommitResponse:
        client = self._require_client()
        return await self._execute(client.get_comments_for_compared_commit, request, CodeCommitGetCommentsForComparedCommitResponse)

    async def get_comments_for_compared_commit_paginated(
        self,
        request: CodeCommitGetCommentsForComparedCommitRequest,
    ) -> list[CodeCommitGetCommentsForComparedCommitResponse]:
        return await self._paginate('get_comments_for_compared_commit', request, CodeCommitGetCommentsForComparedCommitResponse)

    async def get_comments_for_pull_request(
        self,
        request: CodeCommitGetCommentsForPullRequestRequest,
    ) -> CodeCommitGetCommentsForPullRequestResponse:
        client = self._require_client()
        return await self._execute(client.get_comments_for_pull_request, request, CodeCommitGetCommentsForPullRequestResponse)

    async def get_comments_for_pull_request_paginated(
        self,
        request: CodeCommitGetCommentsForPullRequestRequest,
    ) -> list[CodeCommitGetCommentsForPullRequestResponse]:
        return await self._paginate('get_comments_for_pull_request', request, CodeCommitGetCommentsForPullRequestResponse)

    async def get_commit(
        self,
        request: CodeCommitGetCommitRequest,
    ) -> CodeCommitGetCommitResponse:
        client = self._require_client()
        return await self._execute(client.get_commit, request, CodeCommitGetCommitResponse)

    async def get_differences(
        self,
        request: CodeCommitGetDifferencesRequest,
    ) -> CodeCommitGetDifferencesResponse:
        client = self._require_client()
        return await self._execute(client.get_differences, request, CodeCommitGetDifferencesResponse)

    async def get_differences_paginated(
        self,
        request: CodeCommitGetDifferencesRequest,
    ) -> list[CodeCommitGetDifferencesResponse]:
        return await self._paginate('get_differences', request, CodeCommitGetDifferencesResponse)

    async def get_file(
        self,
        request: CodeCommitGetFileRequest,
    ) -> CodeCommitGetFileResponse:
        client = self._require_client()
        return await self._execute(client.get_file, request, CodeCommitGetFileResponse)

    async def get_folder(
        self,
        request: CodeCommitGetFolderRequest,
    ) -> CodeCommitGetFolderResponse:
        client = self._require_client()
        return await self._execute(client.get_folder, request, CodeCommitGetFolderResponse)

    async def get_merge_commit(
        self,
        request: CodeCommitGetMergeCommitRequest,
    ) -> CodeCommitGetMergeCommitResponse:
        client = self._require_client()
        return await self._execute(client.get_merge_commit, request, CodeCommitGetMergeCommitResponse)

    async def get_merge_conflicts(
        self,
        request: CodeCommitGetMergeConflictsRequest,
    ) -> CodeCommitGetMergeConflictsResponse:
        client = self._require_client()
        return await self._execute(client.get_merge_conflicts, request, CodeCommitGetMergeConflictsResponse)

    async def get_merge_options(
        self,
        request: CodeCommitGetMergeOptionsRequest,
    ) -> CodeCommitGetMergeOptionsResponse:
        client = self._require_client()
        return await self._execute(client.get_merge_options, request, CodeCommitGetMergeOptionsResponse)

    async def get_pull_request(
        self,
        request: CodeCommitGetPullRequestRequest,
    ) -> CodeCommitGetPullRequestResponse:
        client = self._require_client()
        return await self._execute(client.get_pull_request, request, CodeCommitGetPullRequestResponse)

    async def get_pull_request_approval_states(
        self,
        request: CodeCommitGetPullRequestApprovalStatesRequest,
    ) -> CodeCommitGetPullRequestApprovalStatesResponse:
        client = self._require_client()
        return await self._execute(client.get_pull_request_approval_states, request, CodeCommitGetPullRequestApprovalStatesResponse)

    async def get_pull_request_override_state(
        self,
        request: CodeCommitGetPullRequestOverrideStateRequest,
    ) -> CodeCommitGetPullRequestOverrideStateResponse:
        client = self._require_client()
        return await self._execute(client.get_pull_request_override_state, request, CodeCommitGetPullRequestOverrideStateResponse)

    async def get_repository(
        self,
        request: CodeCommitGetRepositoryRequest,
    ) -> CodeCommitGetRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.get_repository, request, CodeCommitGetRepositoryResponse)

    async def get_repository_triggers(
        self,
        request: CodeCommitGetRepositoryTriggersRequest,
    ) -> CodeCommitGetRepositoryTriggersResponse:
        client = self._require_client()
        return await self._execute(client.get_repository_triggers, request, CodeCommitGetRepositoryTriggersResponse)

    async def list_approval_rule_templates(
        self,
        request: CodeCommitListApprovalRuleTemplatesRequest | None = None,
    ) -> CodeCommitListApprovalRuleTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_approval_rule_templates, request, CodeCommitListApprovalRuleTemplatesResponse)

    async def list_associated_approval_rule_templates_for_repository(
        self,
        request: CodeCommitListAssociatedApprovalRuleTemplatesForRepositoryRequest,
    ) -> CodeCommitListAssociatedApprovalRuleTemplatesForRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_approval_rule_templates_for_repository, request, CodeCommitListAssociatedApprovalRuleTemplatesForRepositoryResponse)

    async def list_branches(
        self,
        request: CodeCommitListBranchesRequest,
    ) -> CodeCommitListBranchesResponse:
        client = self._require_client()
        return await self._execute(client.list_branches, request, CodeCommitListBranchesResponse)

    async def list_branches_paginated(
        self,
        request: CodeCommitListBranchesRequest,
    ) -> list[CodeCommitListBranchesResponse]:
        return await self._paginate('list_branches', request, CodeCommitListBranchesResponse)

    async def list_file_commit_history(
        self,
        request: CodeCommitListFileCommitHistoryRequest,
    ) -> CodeCommitListFileCommitHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_file_commit_history, request, CodeCommitListFileCommitHistoryResponse)

    async def list_pull_requests(
        self,
        request: CodeCommitListPullRequestsRequest,
    ) -> CodeCommitListPullRequestsResponse:
        client = self._require_client()
        return await self._execute(client.list_pull_requests, request, CodeCommitListPullRequestsResponse)

    async def list_pull_requests_paginated(
        self,
        request: CodeCommitListPullRequestsRequest,
    ) -> list[CodeCommitListPullRequestsResponse]:
        return await self._paginate('list_pull_requests', request, CodeCommitListPullRequestsResponse)

    async def list_repositories(
        self,
        request: CodeCommitListRepositoriesRequest | None = None,
    ) -> CodeCommitListRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.list_repositories, request, CodeCommitListRepositoriesResponse)

    async def list_repositories_paginated(
        self,
        request: CodeCommitListRepositoriesRequest | None = None,
    ) -> list[CodeCommitListRepositoriesResponse]:
        return await self._paginate('list_repositories', request, CodeCommitListRepositoriesResponse)

    async def list_repositories_for_approval_rule_template(
        self,
        request: CodeCommitListRepositoriesForApprovalRuleTemplateRequest,
    ) -> CodeCommitListRepositoriesForApprovalRuleTemplateResponse:
        client = self._require_client()
        return await self._execute(client.list_repositories_for_approval_rule_template, request, CodeCommitListRepositoriesForApprovalRuleTemplateResponse)

    async def list_tags_for_resource(
        self,
        request: CodeCommitListTagsForResourceRequest,
    ) -> CodeCommitListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CodeCommitListTagsForResourceResponse)

    async def merge_branches_by_fast_forward(
        self,
        request: CodeCommitMergeBranchesByFastForwardRequest,
    ) -> CodeCommitMergeBranchesByFastForwardResponse:
        client = self._require_client()
        return await self._execute(client.merge_branches_by_fast_forward, request, CodeCommitMergeBranchesByFastForwardResponse)

    async def merge_branches_by_squash(
        self,
        request: CodeCommitMergeBranchesBySquashRequest,
    ) -> CodeCommitMergeBranchesBySquashResponse:
        client = self._require_client()
        return await self._execute(client.merge_branches_by_squash, request, CodeCommitMergeBranchesBySquashResponse)

    async def merge_branches_by_three_way(
        self,
        request: CodeCommitMergeBranchesByThreeWayRequest,
    ) -> CodeCommitMergeBranchesByThreeWayResponse:
        client = self._require_client()
        return await self._execute(client.merge_branches_by_three_way, request, CodeCommitMergeBranchesByThreeWayResponse)

    async def merge_pull_request_by_fast_forward(
        self,
        request: CodeCommitMergePullRequestByFastForwardRequest,
    ) -> CodeCommitMergePullRequestByFastForwardResponse:
        client = self._require_client()
        return await self._execute(client.merge_pull_request_by_fast_forward, request, CodeCommitMergePullRequestByFastForwardResponse)

    async def merge_pull_request_by_squash(
        self,
        request: CodeCommitMergePullRequestBySquashRequest,
    ) -> CodeCommitMergePullRequestBySquashResponse:
        client = self._require_client()
        return await self._execute(client.merge_pull_request_by_squash, request, CodeCommitMergePullRequestBySquashResponse)

    async def merge_pull_request_by_three_way(
        self,
        request: CodeCommitMergePullRequestByThreeWayRequest,
    ) -> CodeCommitMergePullRequestByThreeWayResponse:
        client = self._require_client()
        return await self._execute(client.merge_pull_request_by_three_way, request, CodeCommitMergePullRequestByThreeWayResponse)

    async def override_pull_request_approval_rules(
        self,
        request: CodeCommitOverridePullRequestApprovalRulesRequest,
    ) -> CodeCommitOverridePullRequestApprovalRulesResponse:
        client = self._require_client()
        return await self._execute(client.override_pull_request_approval_rules, request, CodeCommitOverridePullRequestApprovalRulesResponse)

    async def post_comment_for_compared_commit(
        self,
        request: CodeCommitPostCommentForComparedCommitRequest,
    ) -> CodeCommitPostCommentForComparedCommitResponse:
        client = self._require_client()
        return await self._execute(client.post_comment_for_compared_commit, request, CodeCommitPostCommentForComparedCommitResponse)

    async def post_comment_for_pull_request(
        self,
        request: CodeCommitPostCommentForPullRequestRequest,
    ) -> CodeCommitPostCommentForPullRequestResponse:
        client = self._require_client()
        return await self._execute(client.post_comment_for_pull_request, request, CodeCommitPostCommentForPullRequestResponse)

    async def post_comment_reply(
        self,
        request: CodeCommitPostCommentReplyRequest,
    ) -> CodeCommitPostCommentReplyResponse:
        client = self._require_client()
        return await self._execute(client.post_comment_reply, request, CodeCommitPostCommentReplyResponse)

    async def put_comment_reaction(
        self,
        request: CodeCommitPutCommentReactionRequest,
    ) -> CodeCommitPutCommentReactionResponse:
        client = self._require_client()
        return await self._execute(client.put_comment_reaction, request, CodeCommitPutCommentReactionResponse)

    async def put_file(
        self,
        request: CodeCommitPutFileRequest,
    ) -> CodeCommitPutFileResponse:
        client = self._require_client()
        return await self._execute(client.put_file, request, CodeCommitPutFileResponse)

    async def put_repository_triggers(
        self,
        request: CodeCommitPutRepositoryTriggersRequest,
    ) -> CodeCommitPutRepositoryTriggersResponse:
        client = self._require_client()
        return await self._execute(client.put_repository_triggers, request, CodeCommitPutRepositoryTriggersResponse)

    async def tag_resource(
        self,
        request: CodeCommitTagResourceRequest,
    ) -> CodeCommitTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CodeCommitTagResourceResponse)

    async def test_repository_triggers(
        self,
        request: CodeCommitTestRepositoryTriggersRequest,
    ) -> CodeCommitTestRepositoryTriggersResponse:
        client = self._require_client()
        return await self._execute(client.test_repository_triggers, request, CodeCommitTestRepositoryTriggersResponse)

    async def untag_resource(
        self,
        request: CodeCommitUntagResourceRequest,
    ) -> CodeCommitUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CodeCommitUntagResourceResponse)

    async def update_approval_rule_template_content(
        self,
        request: CodeCommitUpdateApprovalRuleTemplateContentRequest,
    ) -> CodeCommitUpdateApprovalRuleTemplateContentResponse:
        client = self._require_client()
        return await self._execute(client.update_approval_rule_template_content, request, CodeCommitUpdateApprovalRuleTemplateContentResponse)

    async def update_approval_rule_template_description(
        self,
        request: CodeCommitUpdateApprovalRuleTemplateDescriptionRequest,
    ) -> CodeCommitUpdateApprovalRuleTemplateDescriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_approval_rule_template_description, request, CodeCommitUpdateApprovalRuleTemplateDescriptionResponse)

    async def update_approval_rule_template_name(
        self,
        request: CodeCommitUpdateApprovalRuleTemplateNameRequest,
    ) -> CodeCommitUpdateApprovalRuleTemplateNameResponse:
        client = self._require_client()
        return await self._execute(client.update_approval_rule_template_name, request, CodeCommitUpdateApprovalRuleTemplateNameResponse)

    async def update_comment(
        self,
        request: CodeCommitUpdateCommentRequest,
    ) -> CodeCommitUpdateCommentResponse:
        client = self._require_client()
        return await self._execute(client.update_comment, request, CodeCommitUpdateCommentResponse)

    async def update_default_branch(
        self,
        request: CodeCommitUpdateDefaultBranchRequest,
    ) -> CodeCommitUpdateDefaultBranchResponse:
        client = self._require_client()
        return await self._execute(client.update_default_branch, request, CodeCommitUpdateDefaultBranchResponse)

    async def update_pull_request_approval_rule_content(
        self,
        request: CodeCommitUpdatePullRequestApprovalRuleContentRequest,
    ) -> CodeCommitUpdatePullRequestApprovalRuleContentResponse:
        client = self._require_client()
        return await self._execute(client.update_pull_request_approval_rule_content, request, CodeCommitUpdatePullRequestApprovalRuleContentResponse)

    async def update_pull_request_approval_state(
        self,
        request: CodeCommitUpdatePullRequestApprovalStateRequest,
    ) -> CodeCommitUpdatePullRequestApprovalStateResponse:
        client = self._require_client()
        return await self._execute(client.update_pull_request_approval_state, request, CodeCommitUpdatePullRequestApprovalStateResponse)

    async def update_pull_request_description(
        self,
        request: CodeCommitUpdatePullRequestDescriptionRequest,
    ) -> CodeCommitUpdatePullRequestDescriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_pull_request_description, request, CodeCommitUpdatePullRequestDescriptionResponse)

    async def update_pull_request_status(
        self,
        request: CodeCommitUpdatePullRequestStatusRequest,
    ) -> CodeCommitUpdatePullRequestStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_pull_request_status, request, CodeCommitUpdatePullRequestStatusResponse)

    async def update_pull_request_title(
        self,
        request: CodeCommitUpdatePullRequestTitleRequest,
    ) -> CodeCommitUpdatePullRequestTitleResponse:
        client = self._require_client()
        return await self._execute(client.update_pull_request_title, request, CodeCommitUpdatePullRequestTitleResponse)

    async def update_repository_description(
        self,
        request: CodeCommitUpdateRepositoryDescriptionRequest,
    ) -> CodeCommitUpdateRepositoryDescriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_repository_description, request, CodeCommitUpdateRepositoryDescriptionResponse)

    async def update_repository_encryption_key(
        self,
        request: CodeCommitUpdateRepositoryEncryptionKeyRequest,
    ) -> CodeCommitUpdateRepositoryEncryptionKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_repository_encryption_key, request, CodeCommitUpdateRepositoryEncryptionKeyResponse)

    async def update_repository_name(
        self,
        request: CodeCommitUpdateRepositoryNameRequest,
    ) -> CodeCommitUpdateRepositoryNameResponse:
        client = self._require_client()
        return await self._execute(client.update_repository_name, request, CodeCommitUpdateRepositoryNameResponse)
