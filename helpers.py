import json


def db_users_to_json(rows):
    json_result = []
    for row in rows:
        user_data = {
            'id': row[0],
            'user_name': row[1]
        }
        json_result.append(user_data)
    if len(json_result) == 1:
        return json.dumps(json_result[0])
    else:
        return json.dumps(json_result)