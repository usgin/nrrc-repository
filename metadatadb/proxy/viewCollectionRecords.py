from django.http import HttpResponseNotAllowed
from metadatadb.proxy import proxyRequest, hide_unpublished

def viewCollectionRecords(req, resourceId, viewFormat):
    if req.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    kwargs = {
        'path': '/metadata/collection/' + resourceId + '/records.' + viewFormat,
        'method': req.method         
    }
    if viewFormat == 'iso.xml': viewFormat = 'waf'
    return hide_unpublished(req.user, proxyRequest(**kwargs), viewFormat)