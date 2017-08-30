from django.db.backends.signals import connection_created


def activate_foreign_keys(sender, connection, **kwargs):
    """Enable integrity constraint with sqlite."""
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA temp_store = memory;')
        cursor.execute('PRAGMA synchronous = normal;')
        cursor.execute('PRAGMA threads = 4;')


connection_created.connect(activate_foreign_keys)
