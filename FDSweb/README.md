# FDS web

# Dependencies
- /opt/fds/web_info.json
    ``` json
    {
        "domain_name": "127.0.0.1:8000",
        "FDS_ENV": "dev",
        "FDS_SECRET_KEY": "...",
        "FDS_MYSQL_DBNAME": "fdsweb",
        "FDS_MYSQL_USER": "...",
        "FDS_MYSQL_PASSWORD": "...",
        "EMAIL_HOST_USER": "...",
        "EMAIL_HOST_PASSWORD": "...",
        "GEOIP_PATH": "...",
        "google_app_client_id": "...",
        "google_app_client_secret": "..."
    }
    ```
- Geoip2:
    + Download GeoLite2 City and GeoLite2 Country gzip files from https://dev.maxmind.com/geoip/geoip2/geolite2/
    + Extract and put them to the GEOIP_PATH which is defined in /opt/fds/web_info.json
- django-tracking-analyzer: `pip install django-tracking-analyzer`
    + change anaconda3/lib/python3.7/site-packages/tracking_analyzer/admin.py: line 200-208 to:
        ```python
        current_results = []
        objs = Tracker.objects.filter(pk__in=list(current_pks))
        for i in range(len(objs)):
            current_results.append({'date': objs[i].timestamp.isoformat()[:16], 'requests': i+1 })
        ```
- user-agents:
    + `pip install pyyaml ua-parser user-agents`
    + `pip install django-user-agents`