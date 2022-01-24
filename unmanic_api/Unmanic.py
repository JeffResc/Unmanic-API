import urllib3
import json

class Unmanic:
    def __init__(self, host='localhost', port=8888, use_ssl=False, ignore_ssl_cert=False):
        # Check types for sanity
        if not isinstance(host, str):
            raise TypeError('"host" must be a string')
        if not isinstance(port, int):
            raise Exception('"port" must be of type integer')
        if not isinstance(use_ssl, bool):
            raise Exception('"use_ssl" must be of type boolean')
        if not isinstance(ignore_ssl_cert, bool):
            raise Exception('"ignore_ssl_cert" must be of type boolean')

        # Set connection protocol
        if not use_ssl:
            proto = 'http'
        else:
            proto = 'https'

        # Set base URL for contacting the API
        self.base_url = proto + '://' + host + ':' + str(port) + '/unmanic/api/v2'

        # Set up HTTP connection pool
        self.ignore_ssl_cert = ignore_ssl_cert
        self.http = urllib3.PoolManager()

        # Perform a test connection to the API (get version)
        try:
            self.get_version()
        except:
            raise Exception('Could not connect to API')
        

    # Get version of the API
    def get_version(self):
        if self.ignore_ssl_cert:
            r = self.http.request('GET', self.base_url + '/version/read', cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('GET', self.base_url + '/version/read')
        if r.status == 200:
            return json.loads(r.data.decode('utf-8'))['version']
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Pause a worker, provided its ID (e.g. 'W0', 'W1', etc.)
    def pause_worker(self, worker_id):
        if self.ignore_ssl_cert:
            r = self.http.request('POST', self.base_url + '/workers/worker/pause', headers={'Content-Type': 'application/json'}, body=json.dumps({'worker_id': worker_id}), cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('POST', self.base_url + '/workers/worker/pause', headers={'Content-Type': 'application/json'}, body=json.dumps({'worker_id': worker_id}))
        if r.status == 200:
            return True
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Pause all workers
    def pause_all_workers(self):
        if self.ignore_ssl_cert:
            r = self.http.request('POST', self.base_url + '/workers/worker/pause/all', cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('POST', self.base_url + '/workers/worker/pause/all')
        if r.status == 200:
            return True
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Resume a worker, provided its ID (e.g. 'W0', 'W1', etc.)
    def resume_worker(self, worker_id):
        if self.ignore_ssl_cert:
            r = self.http.request('POST', self.base_url + '/workers/worker/resume', headers={'Content-Type': 'application/json'}, body=json.dumps({'worker_id': worker_id}), cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('POST', self.base_url + '/workers/worker/resume', headers={'Content-Type': 'application/json'}, body=json.dumps({'worker_id': worker_id}))
        if r.status == 200:
            return True
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Resume all workers
    def resume_all_workers(self):
        if self.ignore_ssl_cert:
            r = self.http.request('POST', self.base_url + '/workers/worker/resume/all', cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('POST', self.base_url + '/workers/worker/resume/all')
        if r.status == 200:
            return True
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Terminate a worker, provided its ID (e.g. 'W0', 'W1', etc.)
    def terminate_worker(self, worker_id):
        if self.ignore_ssl_cert:
            r = self.http.request('POST', self.base_url + '/workers/worker/terminate', headers={'Content-Type': 'application/json'}, body=json.dumps({'worker_id': worker_id}), cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('POST', self.base_url + '/workers/worker/terminate', headers={'Content-Type': 'application/json'}, body=json.dumps({'worker_id': worker_id}))
        if r.status == 200:
            return True
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Get status of all workers
    def get_workers_status(self):
        if self.ignore_ssl_cert:
            r = self.http.request('GET', self.base_url + '/workers/status', cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('GET', self.base_url + '/workers/status')
        if r.status == 200:
            return json.loads(r.data.decode('utf-8'))['workers_status']
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Get number of workers
    def get_workers_count(self):
        if self.ignore_ssl_cert:
            r = self.http.request('GET', self.base_url + '/settings/read', cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('GET', self.base_url + '/settings/read')
        if r.status == 200:
            return json.loads(r.data.decode('utf-8'))['settings']['number_of_workers']
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))

    # Set number of workers
    def set_workers_count(self, number_of_workers):
        if self.ignore_ssl_cert:
            r = self.http.request('POST', self.base_url + '/settings/write', headers={'Content-Type': 'application/json'}, body=json.dumps({'settings': {'number_of_workers': number_of_workers}}), cert_reqs='CERT_NONE', assert_hostname=False)
        else:
            r = self.http.request('POST', self.base_url + '/settings/write', headers={'Content-Type': 'application/json'}, body=json.dumps({'settings': {'number_of_workers': number_of_workers}}))
        if r.status == 200:
            return True
        else:
            raise Exception('API returned an error, HTTP error code: ' + str(r.status))
