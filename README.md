# TuringMachine
Autores:
Guilherme Gaiardo (https://github.com/GuiGaiardo)
Matheus Garay Trindade (https://github.com/mgt1g13)


Este projeto é parte de um trabalho da cadeira de Teoria da Computação, do curso de Ciência da Computação da
Universidade Federal de Santa Maria.
O objetivo é simular uma Máquina de Turing (MT) com múltiplas fitas. A MT pode ser Reconhecedora de Linguagens ou
Processadora de Funções.
Um dos requisitos do projeto é que sejam utilizadas multiplas threads para realizar tarefas em paralelo.
As partes paralelizadas serão duas: checagem dos pre-requisitos das Funcoes de Transicao e
realizar as operacoes nas multiplas fitas da MT.

A ideia geral do programa pode ser entendida com o diagrama (arquivo Diagrama.xml) que pode ser aberto em https://www.draw.io/.
(completar a descrição)


Ela receberá em sua entrada padrão (STD IN) as seguintes informações:

1 #Número de fitas
5 3 4 13 #No de estados, No de simbolos no alfabeto de entrada, No de simbolos no alfabeto da fita e No de funcoes de transicao
q1 q2 q3 q4 qac #Estados (qac = estado de aceite)
a b # #alfabeto de entrada
a b # B #alfabeto da fita
(q1,a)=(q1,a,D) #Estados de transicao
(q1,b)=(q1,b,D)
(q1,#)=(q1,#,D)
(q1,B)=(q2,B,E)
(q2,a)=(q3,B,E)
(q2,b)=(q4,B,E)
(q2,#)=(qac,B,E)
(q3,a)=(q3,a,E)
(q3,b)=(q4,a,E)
(q3,#)=(qac,a,E)
(q4,b)=(q4,b,E)
(q4,a)=(q3,b,E)
(q4,#)=(qac,b,E)
P #P = Processadora de funcões, R = Reconhecedora de linguagens
3 #No de entradas para teste
aaaba#ababbb #Entradas
aaaabbb
bbab#aab


E gerará uma saída com o seguinte padrão:

aceita #estado de aceite
rejeita #estado de rejeicao
aaabaababbb #fita com a saida (processamento de funcao)
