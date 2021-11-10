def get_object(Model, id) -> object or None:
    try:
        model = Model.objects.get(id=id)
    except Exception:
        return None
    else:
        return model
    
    
def getSchooling(id) -> str or None:
    SCHOOLING_CHOICES = [
        {'name': 'Ensino Fundamental', 'id': 1},
        {'name': 'Ensino Médio', 'id': 2},
        {'name': 'Ensino Superior', 'id': 3},
    ]
    result = [x['name'] for x in SCHOOLING_CHOICES if x['id'] == id]
    return result[0] if result else None
    