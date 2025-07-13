class Solution:
    def maxProfit(self, precos: List[int]) -> int:
        if not precos:
            return 0

        dias = len(precos)
        transacao1 = [0] * dias
        transacao2 = [0] * dias

        # Lucro máximo até o dia i (1ª transação)
        preco_minimo = precos[0]
        for i in range(1, dias):
            preco_minimo = min(preco_minimo, precos[i])
            transacao1[i] = max(transacao1[i - 1], precos[i] - preco_minimo)

        # Lucro máximo a partir do dia i (2ª transação)
        preco_maximo = precos[-1]
        for i in range(dias - 2, -1, -1):
            preco_maximo = max(preco_maximo, precos[i])
            transacao2[i] = max(transacao2[i + 1], preco_maximo - precos[i])

        # Lucro máximo combinando as duas transações
        lucro_maximo = 0
        for i in range(dias):
            lucro_maximo = max(lucro_maximo, transacao1[i] + transacao2[i])

        return lucro_maximo