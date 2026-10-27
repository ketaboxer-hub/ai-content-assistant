def get_missing_fields(project):
    required_fields = ["title", "idea", "status"]
    fields = []

    for field in required_fields:
    
        if field not in project:
            fields.append(field)

    return fields

def get_invalid_fields(project):
    missing_invalids = ["title", "idea", "status"]
    invalids = []

    for invalid in missing_invalids:
        if not isinstance(project[invalid], str):
            invalids.append(invalid)
        elif project[invalid].strip() == "":
            invalids.append(invalid)
    return invalids