from api import mapping




def searchuser(id):
    body = {"query": {"match_phrase": {"email":id}}}
    result = mapping.elasticSearch('user-index',body)
    result = result['hits']
    if result['total'] >= 1:
        return True
    return False




def logincheck(id,password):
    body = {"query": {
            "bool": {
                "must": { "match_phrase": { "email": id }},
                "must": { "match_phrase": { "password":  password }}
                }
            }
        }
    result = mapping.elasticSearch('user-index',body)
    result = result['hits']
    if result['total'] >= 1:
        #print result
        hits = result['hits']
        if hits:
            for hit in hits:
                userid = hit['_id']
                break
        return userid
    return False

def insertuser(data):
    return mapping.elasticInsert('user-index','user',data)

def listofusers():
    result_list = []
    result = mapping.elasticSearch('user-index')
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            firstName = hit['_source']['firstName']
            lastName = hit['_source']['lastName']
            email = hit['_source']['email']
            password = hit['_source']['password']
            result_list.append(dict(firstName=firstName, lastName=lastName, email=email, password=password,userid=_id))
    return result_list
