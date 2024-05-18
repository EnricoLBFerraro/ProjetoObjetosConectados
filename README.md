# ProjetoObjetosConectados
## Descrição
O projeto CardioMonitor utiliza um Arduino UNO conectado a um Pulse Sensor e um display LCD para monitorar a frequência cardíaca em tempo real. O Pulse Sensor detecta o ritmo cardíaco, que são processados pelo Arduino UNO. Esses dados são exibidos no LCD, proporcionando uma leitura instantânea da frequência cardíaca. Além disso, o Arduino se comunica com um servidor Flask via porta serial, permitindo que os dados de BPM sejam acessados e visualizados através de uma interface web. O projeto combina hardware e software para criar uma solução prática de monitoramento cardíaco.
## HardWare
### PulseSensor
O Pulse Sensor é um sensor biométrico projetado para medir a frequência cardíaca. Ele utiliza um fotodiodo e um LED para detectar as mudanças no volume sanguíneo no dedo ou lóbulo da orelha, gerando um sinal analógico correspondente aos batimentos cardíacos. Este sensor é ideal para aplicações em saúde e fitness, sendo fácil de integrar com microcontroladores como o Arduino.
### Arduino UNO
O Arduino Uno é uma plataforma de prototipagem eletrônica baseada em hardware e software de código aberto. Ele é equipado com um microcontrolador ATmega328P, oferecendo 14 pinos digitais de entrada/saída (dos quais 6 podem ser usados como saídas PWM), 6 entradas analógicas, um cristal oscilador de 16 MHz, uma conexão USB, um conector de energia, um conector ICSP e um botão de reset. O Arduino Uno é amplamente utilizado devido à sua simplicidade, flexibilidade e compatibilidade com uma vasta gama de sensores e módulos.
### Display LCD 16x2
O Display LCD 16x2 é uma tela de cristal líquido capaz de mostrar 16 caracteres por linha em duas linhas. Ele é frequentemente usado em projetos eletrônicos para exibir informações diretamente. Este display é fácil de conectar ao Arduino e é controlado através de uma interface paralela, utilizando um conjunto de comandos específicos para escrever e manipular os caracteres exibidos. O LCD 16x2 é ideal para mostrar dados em tempo real, como a frequência cardíaca monitorada pelo Pulse Sensor.

## Comunicação e Código
O Arduino se comunica com um servidor Flask via porta serial, permitindo que os dados de BPM sejam acessados e visualizados através de uma interface web. Já o código configura um servidor Flask que se comunica com um Arduino via porta serial para obter dados de frequência cardíaca. Ele serve uma página web principal e fornece uma rota para acessar os dados de BPM em formato JSON, permitindo a visualização e monitoramento da frequência cardíaca através de uma interface web.
