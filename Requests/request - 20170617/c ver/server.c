#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

/*** SECTION 1 - GRAPH OBJECT ***/
// reference: http://www.geeksforgeeks.org/graph-and-its-representations/
// modification: add length to addEdge function and AdjListNode ... etc

////////////////////////////////////////////////////////////////////////////////

// A C Program to demonstrate adjacency list representation of graphs
// A structure to represent an adjacency list node
struct AdjListNode
{
    int dest;
    int length;
    struct AdjListNode* next;
};

// A structure to represent an adjacency list
struct AdjList
{
    struct AdjListNode *head;  // pointer to head node of list
};

// A structure to represent a graph. A graph is an array of adjacency lists.
// Size of array will be V (number of vertices in graph)
struct Graph
{
    int V;
    struct AdjList* array;
};

// A utility function to create a new adjacency list node
struct AdjListNode* newAdjListNode(int dest, int length)
{
    struct AdjListNode* newNode =
            (struct AdjListNode*) malloc(sizeof(struct AdjListNode));
    newNode->dest = dest;
    newNode->length = length;
    newNode->next = NULL;
    return newNode;
}

// A utility function that creates a graph of V vertices
struct Graph* createGraph(int V)
{
    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
    graph->V = V;

    // Create an array of adjacency lists.  Size of array will be V
    graph->array = (struct AdjList*) malloc(V * sizeof(struct AdjList));

     // Initialize each adjacency list as empty by making head as NULL
    int i;
    for (i = 0; i < V; ++i)
        graph->array[i].head = NULL;

    return graph;
}

// Adds an edge to an undirected graph
void addEdge(struct Graph* graph, int src, int dest, int length)
{
    // Add an edge from src to dest.  A new node is added to the adjacency
    // list of src.  The node is added at the begining
    struct AdjListNode* newNode = newAdjListNode(dest, length);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    // Since graph is undirected, add an edge from dest to src also
    newNode = newAdjListNode(src, length);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}
// A utility function to print the adjacenncy list representation of graph
void printGraph(struct Graph* graph)
{
    int v;
    for (v = 0; v < graph->V; ++v)
    {
        struct AdjListNode* pCrawl = graph->array[v].head;
        printf("\n Adjacency list of vertex %d\n head ", v);
        while (pCrawl)
        {
            printf("-> %d", pCrawl->dest);
            pCrawl = pCrawl->next;
        }
        pCrawl = graph->array[v].head;
        printf("\n Length list of vertex %d\n head ", v);
        while (pCrawl)
        {
            printf("-> %d", pCrawl->length);
            pCrawl = pCrawl->next;
        }
        printf("\n");
    }
}
////////////////////////////////////////////////////////////////////////////////
/*** END OF SECTION 1 ***/

/*** SECTION 2 - DIJKSTRA ALGORITHM ***/
// reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
////////////////////////////////////////////////////////////////////////////////

// Stack w/ Array
void push(int * stack, int * top, int val)
{
        * top += 1;
        stack[*top] = val;
}

int pop(int * stack, int * top)
{

        int val = stack[*top];
        stack[*top] = -1;
        * top -= 1;
        return val;
}
// Dijkstra Algorithm
int* DijkstraAlgorithm(struct Graph* graph, int V, int source, int target)
{
    int Q[V], prev[V];   // initialize vertice set
    float dist[V];
    for(int i=0; i<V; i++)
    {
        Q[i] = i;
        prev[i] = -1; // UNDEFINED node
        dist[i] = INFINITY;
    }

    dist[source] = 0;

    //int n = sizeof(Q) / sizeof(int);
    int n = V;

    while(n > 0) // this will be an inifinit loop if target = 0 (not accessible)
    {
        // find the vertice with lowest cost
        float minDist = INFINITY;
        int u = -1;

        for(int i=0; i<V; i++)
        {
            if(Q[i] != -1 && dist[i] < minDist)
            {
                u = i;
                minDist = dist[i];
            }
        }

        // found target
        if (u == target)
            break;

        // remove the vertice from Q
        Q[u] = -1;
        n--;

        struct AdjListNode* pCrawl = graph->array[u].head;
        while (pCrawl)
        {
            int alt = dist[u] + pCrawl->length;
            if (alt < dist[pCrawl->dest])
            {
                dist[pCrawl->dest] = alt;
                prev[pCrawl->dest] = u;
            }
            pCrawl = pCrawl->next;
        }
    }

    // trace the path from prev using stack
    int stack[V];
    for(int i=0; i<V; i++)
        stack[i] = -1;
    int top = -1;

    int u = target;
    while(prev[u]!=-1)
    {
        push(stack, &top , u);
        u = prev[u];
    }
    push(stack, &top , u);

    // revese
    static int* path;
    path = malloc(V * sizeof(int));
    int ind = 0;
    while(top>=0)
    {
        path[ind] = pop(stack, &top);
        ind += 1;
    }
    return path;
}

void  GetResults(int source, int target, char* sendBuff, int buffLen)
{
    // Generate Graph
    // according to the HW-10-2 requirements
    int V = 11; // 1~10 is used, node 0 is not connected
    struct Graph* graph = createGraph(V);
    addEdge(graph,1, 2, 1);
    addEdge(graph,1, 3, 3);
    addEdge(graph,1, 4, 3);
    addEdge(graph,2, 3, 1);
    addEdge(graph,2, 5, 1);
    addEdge(graph,2, 6, 8);
    addEdge(graph,3, 4, 1);
    addEdge(graph,3, 5, 1);
    addEdge(graph,3, 6, 1);
    addEdge(graph,3, 7, 2);
    addEdge(graph,4, 6, 2);
    addEdge(graph,4, 7, 3);
    addEdge(graph,4, 8, 1);
    addEdge(graph,5, 9, 1);
    addEdge(graph,6, 9, 1);
    addEdge(graph,6, 10, 7);
    addEdge(graph,7, 9, 3);
    addEdge(graph,7, 10, 2);
    addEdge(graph,8, 10, 4);

    // Dijkstra Algorithm
    int * path = DijkstraAlgorithm(graph, V, source, target);

    // append results to the buffer
    // reference: http://www.cplusplus.com/reference/cstdio/snprintf/
    // reference: https://stackoverflow.com/questions/11718573/snprintf-in-a-loop-does-not-work-on-linux
    int ind = 0;
    int offset = 0;
    while(path[ind]!=target)
    {
        offset += snprintf ( sendBuff+offset, buffLen-offset, "%d ", path[ind]);
        ind += 1;
    }
    snprintf ( sendBuff+offset, buffLen-offset, "%d \n", path[ind]);
}

////////////////////////////////////////////////////////////////////////////////
/*** END OF SECTION 2 ***/

/*** SECTION 3 - SERVER CONTROL ***/
// reference: http://www.roman10.net/2011/12/02/simple-tcp-socket-client-and-server-communication-in-c-under-linux/
////////////////////////////////////////////////////////////////////////////////
void nonblock(int sockfd)
{
    int opts;
    opts = fcntl(sockfd, F_GETFL);
    if(opts < 0)
    {
        fprintf(stderr, "fcntl(F_GETFL) failedn");
    }
    opts = (opts | O_NONBLOCK);
    if(fcntl(sockfd, F_SETFL, opts) < 0)
    {
        fprintf(stderr, "fcntl(F_SETFL) failedn");
    }
}

int main(int argc, char *argv[])
{
     int BUFLEN = 2000;
     int sockfd, newsockfd, portno;
     socklen_t clilen;
     char buffer[BUFLEN];
     struct sockaddr_in serv_addr, cli_addr;
     int n, i;
     int one = 1;

     if (argc < 2) {
         fprintf(stderr,"please specify a port numbern");
         exit(1);
     }

     sockfd = socket(AF_INET, SOCK_STREAM, 0);

     if (sockfd < 0) {
        perror("ERROR create socket");
        exit(1);
     }

     setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &one, sizeof one);    //allow reuse of port

     //bind to a local address
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);

     if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
        perror("ERROR on bind");
        exit(1);
     }
     //listen marks the socket as passive socket listening to incoming connections,
     //it allows max 5 backlog connections: backlog connections are pending in queue
     //if pending connections are more than 5, later request may be ignored

     listen(sockfd,1);

     //accept incoming connections

     clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
     //nonblock(newsockfd);        //if we want to set the socket as nonblock, we can uncomment this
     if (newsockfd < 0) {
        perror("ERROR on accept");
        exit(1);
     }

     printf("connection accepted\n");

     int router[2];
     int ind=0;

     for (i = 0; i < 1; ++i)
     {
         int run = 1;
         while(run)
         {
         bzero(buffer,BUFLEN);
         n = read(newsockfd,buffer,BUFLEN);
         if (n < 0) {
            perror("ERROR read from socket");
         }
         //printf("received: %s",buffer);
         router[ind] = atoi(buffer);
         ind += 1;
         if (ind > 1)
            break;
        }

        // received 2 inputs: source and target number of routers
        printf("received source/target: %d / %d\n", router[0], router[1]);
        // calculate the shortest path
        GetResults(router[0], router[1], buffer, BUFLEN);

        n = write(newsockfd, buffer, sizeof(buffer));
        printf("sent path: %s", buffer);
        if (n < 0)
        {
        perror("ERROR write to socket");
        }
     }
     close(newsockfd);
     close(sockfd);
     return 0;
}
////////////////////////////////////////////////////////////////////////////////
/*** END OF SECTION 3 ***/
