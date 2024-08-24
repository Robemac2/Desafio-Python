# Desafio de Projeto Python - Sistema Bancário

---

### Regras de Negócio Versão 1.0

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

---

### Regras de Negócio Versão 2.0

- O sistema deverá implementar as seguintes funcionalidades adicionais:
  - Estabelecer um limite de 10 operações por dia
  - Caso o usuário tente realizar uma operação após o limite diário, o sistema deverá exibir uma mensagem informando que o limite foi atingido
  - Mostrar no extrato a data e hora de cada operação