# Dependency Inversion Principle
O princípio da inversão de dependência diz modulos de nível alto não devem depender de módulos de nível baixo, mas deve depender de abstrações e abstrações não devem depender de detalhes, mas detalhes devem depender de abstrações.

O código não pode depender de implementações, mas sim de abstrações. Ele não deve depender do que acontece "por debaixo dos panos" de uma função, mas sim de uma abstração, de uma interface genérica que intermedia o acesso de uma classe a outra da forma mais abstrata possível.