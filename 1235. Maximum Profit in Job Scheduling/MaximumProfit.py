class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        # Agrupa os trabalhos como tuplas (start, end, profit) e ordena por start time
        trabalhos = sorted(zip(startTime, endTime, profit))

        # Lista apenas com os horários de início (para busca binária)
        inicios = [t[0] for t in trabalhos]

        # Vetor dp para armazenar os resultados da PD
        dp = [0] * (n + 1)

        # Percorre de trás pra frente
        for i in range(n - 1, -1, -1):
            # Encontra o próximo trabalho que começa após o fim do trabalho atual
            j = bisect_left(inicios, trabalhos[i][1])
            
            # Máximo lucro com e sem pegar o trabalho atual
            lucro_com_i = trabalhos[i][2] + dp[j]
            lucro_sem_i = dp[i + 1]
            
            # Escolhe o melhor
            dp[i] = max(lucro_com_i, lucro_sem_i)

        return dp[0]