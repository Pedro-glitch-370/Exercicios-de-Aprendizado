# Roubo na Gaiola Encantada!

É madrugada do dia 31 de Outubro sobre as águas de um rio escuro e profundo. A Gaiola Encantada, o Vapor Fantasma dos riachos brasileiras, conduz dezenas de espíritos errantes e almas perdidas, que terminam de se arrumar para mais um inesquecível Dia das Bruxas com muita festa e guloseima!

Porém, ao chegarem no salão principal da embarcação, presenciam uma cena de arrepiar: **Todos os doces da festa desapareceram!**

As assombrações acusam umas às outras, e o caos rapidamente é estabelecido na Gaiola. Cabe a você, mestre programador sem medo de desafios bestas, desvendar quem é o ladrão guloso que se esconde entre os mais variados tipos de monstros!

# Input

Sabendo que não há saída segura da embarcação, é **altamente provável** que o ladrão continua solto pelos corredores do Gaiola.

Portanto, o programa deve receber uma longa lista contendo as iniciais das assombrações cujas presenças no salão principal foram relatadas por outras.

Dentro da lista, haverão **seis sublistas** contendo **grupos de monstros** que **entraram ou saíram do salão**. Cada sublista será composta **apenas de caracteres**, semelhante ao seguinte exemplo:

> `[['Z', 'O'], ['Z', 'G', 'L', 'F', ...] (list / str)`
> 

Cada sublista também representará uma hora da madrugada gasta na investigação do caso. O horário deve começar das **0h** e seguir até às **5h**.

Os monstros à bordo do Gaiola são: Zumbi (Z), Gárgula (G), Lobisomem (L), Fantasma (F), Vampiro (V), Múmia (M), Bruxa (B), Ciclope (C), Ogro (O), Sereia (S), Troll (T), Espírito (E), Palhaço (P) e Homem do Saco (H).

A primeira aparição de um monstro em uma sublista indica que ele entrou no salão principal. A segunda aparição, a sua saída do salão. A partir da próxima aparição, o padrão se repete.

Essa lógica **pode se repetir inúmeras vezes pela lista**, incluindo a aparição de um mesmo monstro mais de uma vez em uma única sublista.

## Determinação do ladrão

Será **considerado o ladrão** o monstro que, **em qualquer momento da noite**, **tenha ficado sozinho** **no salão**.

**OBS:** Caso a condição acima não se aplique em nenhum momento, então ninguém poderá ser considerado o ladrão, e a investigação se encerrará sem conclusão.

Por fim, um último detalhe: O passar das horas implica ainda mais espera pela tão aguardada festa de Halloween. Por isso, caso o ladrão seja encontrado, a investigação **deve ser encerrada imediatamente** para que as assombrações possam, enfim, celebrar o seu dia!

**OBS1:** É obrigatório o uso de recursão para a resolução da questão.

**OBS2:** A fins de esclarecimento, eval() está permitido para essa questão.

# Output

Antes de tudo, imprima:

> **`Há um impostor entre nós... Que a investigação comece!`**
> 

Ao final de cada hora de investigação (ou seja, ao final de cada sublista analisada), caso o ladrão ainda não tenha sido descoberto, deve-se imprimir:

> **`O relógio bate {horario_atual} horas... A bruma de mistério ainda paira sobre o Gaiola.`**
> 

Por outro lado, caso o ladrão **seja encontrado**, deve-se imprimir:

> **`Elementar, meu caro programa! O criminoso, afinal, é {ladrão}, que roubou sozinho(a) os doces às {horário} horas dessa madrugada!`**
> 

Caso o ladrão **não seja encontrado**, imprima no lugar:

> **`Somente com essas informações, não posso deduzir qual a mente obscura por trás desse caso... São os fatos, madame, apenas os fatos...`**
>