STORE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "petId": {
            "type": "integer"
        },
        "quantity": {
            "type": "integer"
        },
        "shipDate": {
            "type": "string"
        },
        "status": {
            "type": "string",
            "enum": ["placed", "approved", "delivered"]
        },
        "complete": {
            "type": "boolean"
        }
    },
    "required": ["id", "status", "complete"]
}

inventory_schema = {
    "type": "object",
    "properties": {
        "approved": {
            "type": "integer"},
        "delivered": {
            "type": "integer"}
    },
    "required": ["approved", "delivered"]
}
