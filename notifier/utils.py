import json

from entities import ENTITY_TYPES

with open("notify_config.json") as json_file:
    entities_config = json.load(json_file)

    if not entities_config:
        raise Exception("notify_config is empty")


def notify_changes(entity_obj, original_entity_obj, entity_type):
    if not entity_type:
        raise Exception("entity_type required")

    if entity_type not in ENTITY_TYPES:
        raise Exception(f"{entity_type} entity not found")

    if not entity_obj and not original_entity_obj:
        raise Exception("entity_obj AND original_entity_obj cannot be None at the same time")

    entity_config = entities_config[entity_type]
    if not entity_config:
        raise Exception(f"{entity_type} do not have config")

    # check need to notify parent or not
    notify = entity_config.get("notify", entity_type)
    if notify not in ENTITY_TYPES:
        raise Exception(f"{notify} entity not found")

    parent = f"{notify}'s " if notify != entity_type else ''
    changed_object = f"{parent}{entity_type}"

    # check if entity created
    if not original_entity_obj and entity_config.get("when_created"):
        return f"{changed_object} created"

    # check if entity physically deleted
    if not entity_obj and entity_config.get("when_physically_deleted"):
        return f"{changed_object} physically deleted"

    # field checking
    if "fields" in entity_config and isinstance(entity_config["fields"], list):
        for field in entity_config["fields"]:
            if isinstance(field, str):  # is simple change
                if not hasattr(entity_obj, field):  # check if new object has property
                    raise Exception(f"{entity_type}'s new object does not have {field} property")
                if not hasattr(original_entity_obj, field):  # check if old object has property
                    raise Exception(f"{entity_type}'s old object does not have {field} property")

                old_value = getattr(original_entity_obj, field)
                new_value = getattr(entity_obj, field)
                if old_value != new_value:
                    return f"{changed_object} changed"
            elif isinstance(field, dict):  # change from - to
                for field_key, field_value in field.items():
                    if not hasattr(entity_obj, field_key):
                        raise Exception(f"{entity_type}'s new does not have {field_key} property")
                    if not hasattr(original_entity_obj, field_key):
                        raise Exception(f"{entity_type}'s old does not have {field_key} property")

                    old_value = getattr(original_entity_obj, field_key)
                    new_value = getattr(entity_obj, field_key)
                    if old_value == field_value.get("from") and new_value == field_value.get("to"):
                        return f"{changed_object} changed"

    return "No changes detected"
