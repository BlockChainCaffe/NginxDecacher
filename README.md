# NginxDecacher

NginX is a great web server, ofthen used as a reverse proxy with geat caching capabilities.

But the possibility to use the PURGE http method to clear specific cache entries is available only in the commercial (not cheap) version of NginX. Thus I needed a way to purge specific cache entries somehow.

The idea is to use a Python script using Flask and Wsgi that gets the same string NginX uses to build the cache, and use the information to delete the cache file
