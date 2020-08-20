# Open-Closed Principle
O princípio Aberto-Fechado diz que uma classe deve estar aberta para extensões e fechada para modificações. Uma vez construída a classe não deve ser alterada, caso exista especificações determinada classe você deve estender-la implementando/sobrescrevendo tal método.

A classe não deve ter verificações se é do tipo "A", "B" ou "C", mas sim ser a base para outras classes que estenderam/herdaram a mesma para cada uma implementar sua regra de negócio, assim diminuindo o acoplamento.