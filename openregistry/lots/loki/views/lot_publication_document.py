# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    get_file,
    update_file_content_type,
    json_view,
    context_unpack,
    APIResource,
)
from openregistry.lots.core.utils import (
    save_lot, oplotsresource, apply_patch,
)

from openprocurement.api.validation import (
    validate_file_upload,
    validate_document_data,
    validate_patch_document_data,
)
from openregistry.lots.core.validation import (
    validate_lot_document_update_not_by_author_or_lot_owner
)
from openregistry.lots.loki.validation import (
    validate_document_operation_in_not_allowed_lot_status
)


@oplotsresource(name='loki:Lot Publication Documents',
                collection_path='/lots/{lot_id}/publications/{publication_id}/documents',
                path='/lots/{lot_id}/publications/{publication_id}/documents/{document_id}',
                lotType='loki',
                description="Publication related binary files (PDFs, etc.)")
class PublicationDocumentResource(APIResource):

    @json_view(permission='view_lot')
    def collection_get(self):
        """Publication Documents List"""
        if self.request.params.get('all', ''):
            collection_data = [i.serialize("view") for i in self.context.documents]
        else:
            collection_data = sorted(dict([
                (i.id, i.serialize("view"))
                for i in self.context.documents
            ]).values(), key=lambda i: i['dateModified'])
        return {'data': collection_data}

    @json_view(content_type="application/json", permission='upload_lot_publications', validators=(validate_file_upload, validate_document_operation_in_not_allowed_lot_status))
    def collection_post(self):
        """Publication Document Upload"""
        document = self.request.validated['document']
        document.author = self.request.authenticated_role
        document.documentOf = 'lot'
        self.context.documents.append(document)
        if save_lot(self.request):
            self.LOGGER.info('Created publication document {}'.format(document.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'publication_document_create'}, {'document_id': document.id}))
            self.request.response.status = 201
            document_route = self.request.matched_route.name.replace("collection_", "")
            self.request.response.headers['Location'] = self.request.current_route_url(_route_name=document_route, document_id=document.id, _query={})
            return {'data': document.serialize("view")}

    @json_view(permission='view_lot')
    def get(self):
        """Publication Document Read"""
        if self.request.params.get('download'):
            return get_file(self.request)
        document = self.request.validated['document']
        document_data = document.serialize("view")
        document_data['previousVersions'] = [
            i.serialize("view")
            for i in self.request.validated['documents']
            if i.url != document.url
        ]
        return {'data': document_data}

    @json_view(content_type="application/json", permission='upload_lot_publications', validators=(validate_document_data, validate_document_operation_in_not_allowed_lot_status,
               validate_lot_document_update_not_by_author_or_lot_owner))
    def put(self):
        """Publication Document Update"""
        document = self.request.validated['document']
        document.documentOf = 'lot'
        document.author = self.request.authenticated_role
        self.request.validated['publication'].documents.append(document)
        if save_lot(self.request):
            self.LOGGER.info('Updated lot document {}'.format(self.request.context.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'lot_document_put'}))
            return {'data': document.serialize("view")}

    @json_view(content_type="application/json", permission='upload_lot_publications', validators=(validate_patch_document_data,
               validate_document_operation_in_not_allowed_lot_status, validate_lot_document_update_not_by_author_or_lot_owner))
    def patch(self):
        """Publication Document Update"""
        if apply_patch(self.request, src=self.request.context.serialize()):
            update_file_content_type(self.request)
            self.LOGGER.info('Updated lot document {}'.format(self.request.context.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'lot_document_patch'}))
            return {'data': self.request.context.serialize("view")}
