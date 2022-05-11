# Flask app mounted on url prefix

Let's test how to remount a Flask app under a different url prefix with nginx,
without changing the application code. nginx will forward requests under /api to
the flask application. The Flask code doesn't know it will be accessed under the `/api` prefix later on,
it's all configured by the environment (but for Flask we need to use gunicorn and set the SCRIPT_NAME env var).

See the other branches for more examples.


## Quick start

`docker-compose up`


## Expected result

```
$ curl localhost/api/
Hello World!

$ curl localhost/api/test
Index is at: /api/

$ curl localhost/api/json
{
  "index": "http://localhost/api/",
  "self": "http://localhost/api/json"
}

$ curl -i localhost/api/redirect
HTTP/1.1 302 FOUND
…
Location: /api/
…
```

## Chaging the port of flask

1. Change the port on the proxy_pass line in `nginx.conf`
2. Change `HTTP_PORT` in the environments of the `flask` service

## Changing the flask app prefix mount

1. Change the location in `nginx.conf` (for ex. `location /api/v1 {`
2. Change the proxy_pass line to include the new location (`proxy_pass http://flask:5001/api/v1;`)
2. Change `SCRIPT_NAME=/api/v1` in the environments of the `flask` service


## Reference

* https://dlukes.github.io/flask-wsgi-url-prefix.html
* https://docs.gunicorn.org/en/stable/run.html
