# TuringMachine
Autores:<br>
Guilherme Gaiardo (https://github.com/GuiGaiardo) <br>
Matheus Garay Trindade (https://github.com/mgt1g13) <br>


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

1 #Número de fitas<br>
5 3 4 13 #No de estados, No de simbolos no alfabeto de entrada, No de simbolos no alfabeto da fita e No de funcoes de transicao<br>
q1 q2 q3 q4 qac #Estados (qac = estado de aceite)<br>
a b # #alfabeto de entrada<br>
a b # B #alfabeto da fita<br>
(q1,a)=(q1,a,D) #Estados de transicao<br>
(q1,b)=(q1,b,D)<br>
(q1,#)=(q1,#,D)<br>
(q1,B)=(q2,B,E)<br>
(q2,a)=(q3,B,E)<br>
(q2,b)=(q4,B,E)<br>
(q2,#)=(qac,B,E)<br>
(q3,a)=(q3,a,E)<br>
(q3,b)=(q4,a,E)<br>
(q3,#)=(qac,a,E)<br>
(q4,b)=(q4,b,E)<br>
(q4,a)=(q3,b,E)<br>
(q4,#)=(qac,b,E)<br>
P #P = Processadora de funcões, R = Reconhecedora de linguagens<br>
3 #No de entradas para teste<br>
aaaba#ababbb #Entradas<br>
aaaabbb<br>
bbab#aab<br>
<br>
<br>
E gerará uma saída com o seguinte padrão:<br>
<br>
aceita #estado de aceite<br>
rejeita #estado de rejeicao<br>
aaabaababbb #fita com a saida (processamento de funcao)<br>
