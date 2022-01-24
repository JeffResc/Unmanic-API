# Unmanic-API
An implementation of the [Unmanic v2 API](https://github.com/Unmanic/unmanic/tree/master/unmanic/webserver/api_v2) in Python.

Please note that not all features of the v2 API have been implemented, rather a few key endpoints that most users should find useful for automation.

## Installing
```bash
pip install unmanic-api
```

## Example of All Methods
```python
from unmanic_api import Unmanic

# Create an Unmanic API instance, provided an optional server host, server port (defaults shown).
um = Unmanic('localhost', 8888)

# Prints the API version
print(um.get_version())

# Pause a worker, given its ID. Will return True if the operation is successful.
um.pause_worker('W0')

# Pause all workers. Will return True if the operation is successful.
um.pause_all_workers()

# Resume a worker, given its ID. Will return True if the operation is successful.
um.resume_worker('W0')

# Resume all workers. Will return True if the operation is successful.
um.resume_all_workers()

# Terminate a worker, given its ID. Will return True if the operation is successful.
um.terminate_worker('W0')

# Get status of all workers, will return an object.
print(um.get_workers_status())

# Get number of workers, will return an integer.
workers_count = um.get_workers_count()

# Set number of workers. Will return True if the operation is successful.
um.set_workers_count(4)
```

## SSL Examples
```python
# Create an Unmanic API instance with SSL
um = Unmanic('localhost', 8888, use_ssl=True)

# Create an Unmanic API instance with SSL, ignoring SSL certificate
um = Unmanic('localhost', 8888, use_ssl=True, ignore_ssl_cert=True)
```

## See Also
- [PyPi Project](https://pypi.org/project/unmanic-api/)
- [GitHub Project](https://github.com/JeffResc/Unmanic-API)
- [Unmanic API Reference](https://github.com/Unmanic/unmanic/tree/master/unmanic/webserver/api_v2)