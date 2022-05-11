# FastAPI app mounted on url prefix

Let's test how to remount a FastAPI app under a different url prefix with nginx,
without changing the application code. nginx will forward requests under /api to
the fastapi application.


## Quick start

`docker-compose up`


## Expected result

```
$ curl localhost/api/
{"message":"Hello World"}

$ curl localhost/api/test
"Index is at: http://localhost/api/"

$ curl localhost/api/json
{"index":"http://localhost/api/","self":"http://localhost/api/json"}

$ curl -i localhost/api/redirect
HTTP/1.1 307 Temporary Redirect
…
location: http://localhost/api/
…
```

## Chaging the port of fastapi app

1. Change the port on the proxy_pass line in `nginx.conf`
2. Change `HTTP_PORT` in the environments of the `fastapi` service

## Changing the fastapi app prefix mount

1. Change the location in `nginx.conf` (for ex. `location /api/v1 {`
2. Change `ROOT_PATH=/api/v1` in the environments of the `fastapi` service


## Reference

* https://fastapi.tiangolo.com/advanced/behind-a-proxy/
