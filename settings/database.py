DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'ProjectDB',
        'USER': 'sa',
        'PASSWORD': 'your_password',
        'HOST': 'your_sql_server_host',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}