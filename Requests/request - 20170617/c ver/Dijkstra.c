#include "graph.c"
#include <math.h>

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

    // trace the path from prev
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
/*
int main()
{
    // Generate Graph
    // referece: http://www.geeksforgeeks.org/graph-and-its-representations/
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
    // reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    int source = 3;
    int target = 10;
    int * path = DijkstraAlgorithm(graph, V, source, target);

    int ind = 0;
    while(ind < sizeof(path))
    {
        printf("%d ", path[ind]);
        ind += 1;
    }
    printf("\n");
}
*/
