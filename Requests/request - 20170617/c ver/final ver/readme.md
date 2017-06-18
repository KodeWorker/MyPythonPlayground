# Complie the Code
```
gcc server.c -o server
gcc client.c -o client
```

# Run the Compiled Files

Open two terminals and run each of the following files.

## Server
input: <port>
```
./server <port>
```

## Client
inputs: <ip><port>
```
./client <ip><port>
```

While the connection is established, you can follow the client instructions to enter the number of source and target router.
The server will return the shortest path by Dijkstra's Algorithm, and then the connection will be terminated.
