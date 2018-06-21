# Description
Example go gRPC server which pulls stock information from socket.

The socket consumer server and client demonstrate how to use grpc go libraries to
use gRPC to retrieve stock information pulled from a UNIX\ domain socket.

Reference:
* [gRPC Basics: Go](https://grpc.io/docs/tutorials/basic/go.html)
* [stock data using python](https://www.quora.com/Using-Python-whats-the-best-way-to-get-stock-data)

# Run the sample code
To compile and run the server, assuming you are in the root of the socket-consumer-server-example
folder, i.e., .../socket-consumer-server-example/, simply:

```sh
$ go run server/server.go
```

Likewise, to run the client:

```sh
$ go run client/client.go
```

# Optional command line flags
The server and client both take optional command line flags. For example, the
client and server run without TLS by default. To enable TLS:

```sh
$ go run server/server.go -tls=true
```

and

```sh
$ go run client/client.go -tls=true
```
