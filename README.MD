
# Rastreador esportivo

API criada utilizando python e flask para gerar dados falsos a serem usados para simular dados de um rastreador esportivo (em desenvolvimento)




## EndPoints

- **/set-bound** -> Define uma area por meio de 4 pontos (latitude e longitude), para configurar em qual area o endpoint "**/new-data**" deve gerar suas posicoes. 


- **/reset-tracker** -> Sempre ao gerar um novo valor, "**/new-data**" ira somar um valor aleatorio ao atributo distance, oque pode nao ser util para gerar dados de varios atletas, portanto, utilizar essa rota ira resetar o atributo distance, permitindo uma forma de testar simular dados de varios atletas.

- **/new-data** -> Ao ser chamada, retorna um objeto seguindo o seguinte padrao. 

```typescript
    bpm: int, 
    lat: float, 
    log: float, 
    speed: float, 
    time: datetime, 
    distance: float,
```
    Obs: Cada atributo e gerado aletoriamente, embora alguns sigam alguns padroes para que se assemelhe aos possiveis dados gerados pelos sensores.


## Instalacao

Para executar este projeto, basta ter baixado esse repositorio, e ter o docker + docker-compose instalado em sua maquina

## Execution

Para executar o projeto, recomendo utilizar o comando: 

```bash
  docker compose up -d
```
    