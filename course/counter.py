"""

Collections - Counter

Collections -> High performance container datatypes

Counter - Receive a iterable as a parameter and create an object of a type of Collections
which is similar to a Dictionary having as a key the list element passed as a parameter and its values as the quantity
of the amount of occurrences of this element.

"""


# Using Counter

from collections import Counter

list1 = [1, 3, 3, 4, 5, 6, 2, 8, 2, 4, 5, 6, 7, 8, 8, 9, 2]

result = Counter(list1)

print(result)
print(type(result))

print(Counter('Rodrigo Pessoa Cantarino de Oliveira'))


text = """
Mussum Ipsum, cacilds vidis litro abertis. Manduma pindureta quium dia nois paga. Casamentiss faiz 
malandris se pirulitá. Mauris nec dolor in eros commodo tempor. Aenean aliquam molestie leo, vitae iaculis nisl. 
Não sou faixa preta cumpadi, sou preto inteiris, inteiris.

Praesent malesuada urna nisi, quis volutpat erat hendrerit non. Nam vulputate dapibus. Aenean aliquam molestie leo, 
vitae iaculis nisl. Sapien in monti palavris qui num significa nadis i pareci latim. Tá deprimidis, eu conheço uma 
cachacis que pode alegrar sua vidis.

Per aumento de cachacis, eu reclamis. Suco de cevadiss deixa as pessoas mais interessantis.
Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Quem manda na minha terra sou euzis!
"""

words = text.split()

most_common = Counter(words).most_common(5)

print(Counter(words))

print(most_common)

