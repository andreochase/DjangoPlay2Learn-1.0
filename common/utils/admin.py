def append_fields(fieldsets, fieldset, fields):
    for _fieldset in fieldsets:
        if _fieldset[0] == fieldset:
            _fieldset[1]['fields'] += fields
            break
    else: 
        fieldsets = fieldsets + (
            (fieldset, {
                'classes': ('wide',),
                'fields': fields
            }),
        )

    return fieldsets


def remove_fields(fieldsets, fieldset, fields):
    for _fieldset in fieldsets:
        if _fieldset[0] == fieldset:
            field_list = list(_fieldset[1]['fields'])
            for field in fields:
                field_list.remove(field)
            _fieldset[1]['fields'] = tuple(field_list)
            break
    else:
        raise Exception(f'No such fieldset: {fieldset}')

    return fieldsets


def move_fields(fieldsets, from_fieldset, to_fieldset, fields):
    remove_fields(fieldsets, from_fieldset, fields)
    append_fields(fieldsets, to_fieldset, fields)

    return fieldsets
