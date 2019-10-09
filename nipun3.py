def make_graph(e):
    d = {}
    for i in range(e):
        x, y= mi()
        if x not in d:
            d[x]=[y]
        else:
            d[x].append(y)
        if y not in d:
            d[y]=[x]
        else:
            d[y].append(x)
    return d
def gr2(n):
    d = defaultdict(list)
    for i in range(n):
        x, y = mi()
        d[x].append(y)
    return d
def connected_components(graph):
    seen = set()
    def dfs(v):
        vs = set([v])
        component = []
        while vs:
            v = vs.pop()
            seen.add(v)
            vs |= set(graph[v]) - seen
            component.append(v)
        return component

    ans = []
    for v in graph:
        if v not in seen:
            d = dfs(v)
            ans.append(d)
    return ans
def primeFactors(n):
    s = set()
    while n % 2 == 0:
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            s.add(i)
            n = n // i
    if n > 2:
        s.add(n)
    return s
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
def SieveOfEratosthenes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n):
        isPrime[i] = True
    p = 2
    while (p * p <= n):
        if (isPrime[p] == True):
            i = p * p
            while (i <= n):
                isPrime[i] = False
                i += p
        p += 1
    return isPrime
