# Desafio de Projeto Python - Sistema Bancário

---

### Regras de Negócio

- O sistema deverá implementar as seguintes funcionalidades:
  - Realizar Saque
    - O sistema deverá permitir saques apenas de valores positivos
    - O sistema deverá permitir saques apenas de valores menores ou iguais ao saldo disponível
    - O limite de saque R$ 500,00
    - O limite de saques executados por dia é de 3
    - Todos os saques deverão ser registrados em uma variável e exibidos no extrato
  - Realizar Depósito
    - O sistema deverá permitir depósitos apenas de valores positivos
    - Todos os depósitos deverão ser registrados em uma variável e exibidos no extrato
  - Consultar Extrato
    - O sistema deverá exibir o extrato com todas as operações de depośito e saque
    - Os saques deverão ser exibidos com o sinal de negativo
    - Os depósitos deverão ser exibidos com o sinal de positivo
    - As operações deverão ser exibidas na ordem em que foram realizadas
    - O extrato deverá exibir o saldo disponível na conta ao final da listagem