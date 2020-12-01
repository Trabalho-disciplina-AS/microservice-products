import os


def validate_request(request):
    funcs = [
        validate_empty_request,
        validate_request_fields
    ]
    for func in funcs:
        validate, msg = func(request)
        if not validate:
            return validate, msg

    return True, 'OK'

def validate_empty_request(request):
    if not request.json:
        return False, 'Empty request'

    return True, 'OK'


def validate_request_fields(request):
    if request.json.get("service_type") not in ['csv', 'json', 'xml']:
        return False, 'Wrong service type'
        
    if not request.json.get('filename'):
        return False, 'Filename is missing'
  
    if not request.json.get('xml'):
        return False, 'No data found'
    
    return True, 'OK'

