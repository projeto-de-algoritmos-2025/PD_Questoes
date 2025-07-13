from typing import List

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        grafo = [[] for _ in range(n)]
        for u, v in edges:
            grafo[u].append(v)
            grafo[v].append(u)
        
        palpites = set((u, v) for u, v in guesses)
        
        contagem_base = 0
        pilha = [(0, -1)] 
        while pilha:
            u, pai = pilha.pop()
            for v in grafo[u]:
                if v == pai:
                    continue
                if (u, v) in palpites:
                    contagem_base += 1
                pilha.append((v, u))
        
        dp = [0] * n
        dp[0] = contagem_base
        
        pilha = [(0, -1)]
        while pilha:
            u, pai = pilha.pop()
            for v in grafo[u]:
                if v == pai:
                    continue
                dp[v] = dp[u]
                if (u, v) in palpites: 
                    dp[v] -= 1
                if (v, u) in palpites:  
                    dp[v] += 1
                pilha.append((v, u))
        
        return sum(1 for cont in dp if cont >= k)