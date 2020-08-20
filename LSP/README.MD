# Liskov Substitution Principle
O princípio da substituição de Liskov diz:

"_Se **q(x)** é uma propriedade de demonstrável dos objetos **x** de tipo **T**. Então **q(y)** deve ser verdadeiro para objetos **y** de tipo **S** onde **S** é um subtipo de **T**._"

O objetivo desse princípio é você poder substituir uma sub-classe por uma super-classe sem gerar erros. Em outras palavras se determinado código checa o tipo da classe então esse determinado código já feriu o princípio de Liskov.
