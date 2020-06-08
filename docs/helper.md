# Descrição do problema

## Por que dados do Twitter?

O Twitter hoje em dia é uma mina de ouro de dados. Ao contrário de outras plataformas e rede sociais, quase todos os tweets dos usuários são completamente públicos e acessíveis. Essa é uma enorme vantagem se você estiver tentando obter uma considerável massa de dados para executar análises. Os dados do Twitter também são bastante específicos.

## Problema

Sabemos que em tempos de crise, a melhor ferramenta que temos são os dados. Tento isso como consideração, o problema central que temos aqui é a coleta de dados do Twitter que tenham a palavra "covid-19" em seu tweet para que passamos tirar análises e tentar prever que tipo de sentimento uma determinada quantidade de pessoas transmite quando utilizam essa palavra.

## Proposta

Tendo em vista a pandemia ocorrida recentemente, temos como proposta a criação de um analisador sentimental para tweets com a palavra "covid-19" no Twitter e que utiliza o bando de dados NoSQL MondoDB para armazenar as informações coletadas e tratadas.

## Caracterização do banco utilizado

* Dinâmico - sem esquema rígido.
* Orientado a documentos
* Alta performance
* Alta disponibilidade - Replicação
* Alta escalabilidade - Sharding
* Sem junções
* Distribuído

## Vantagem

O NoSQL é mais indicado para aqueles sistemas que tenham necessidades maiores de armazenamento e desempenho. Existem vários tipos de banco NoSql, o MongoDb é um banco Nosql orientado a documento. Esse tipo de banco tem uma performance incrível para escrita e não tão boa para leitura.

### Bom para

* Catálogo de produtos de comércio eletrônico.
* Blogs e gerenciamento de conteúdo.
* Análise em tempo real e registro em alta velocidade, armazenamento em cache e alta escalabilidade.
* Gerenciamento de configurações.
* Manutenção de dados baseados em localização - dados geoespaciais.
* Sites de redes móveis e sociais.
* Requisitos de dados em evolução.
* Objetivos pouco acoplados - o design pode mudar com o tempo.

### Não é tão bom para

* Sistemas altamente transacionais ou onde o modelo de dados é projetado com antecedência.
* Sistemas firmemente acoplados.

## Commandos

**Listando todos os tweets com realizando join com a coleção de sentimentos**

```bash
db.getCollection("covid").aggregate([{$lookup:{
  from: 'sentimental',
  localField: '_id',
  foreignField: 'tweet_id',
  as: 'resultado'
}}])
```

* from: nome da Coleção onde vamos buscar os dados
* localField: nome do atributo usado na condição de igualdade, na coleção origem, aqui chamada de Coleção
* foreignField: nome do atributo usado na condição de igualdade na tabela destino, onde buscaremos os dados
* as: atributo que receberá os novos dados


**Tweets de todas as pessoas que começam com a letra A**

```bash
db.getCollection("covid").find({ "name": { $regex: /^A/ } })
```

**Limitando resultados da consulta**

```bash
db.getCollection("covid").find().limit(5)
```

**Exibindo todos tweets removendo o _id**.

```
db.getCollection("covid").find({}, {_id:0})
```

**Exibindo todos tweets onde o criado tem mais que 10000 de amigos**.

```
db.getCollection("covid").find({ "friends_count": { $gt: 10000 }})
```

# Referências

* https://docs.mongodb.com/
* http://db4beginners.com/blog/consultas-no-mongodb/
* https://stackoverflow.com/questions/25589113/how-to-select-a-single-field-for-all-documents-in-a-mongodb-collection
* https://www.youtube.com/watch?v=_zxwlrYUHr4&t=932s
* http://db4beginners.com/blog/join-no-mongodb/
* https://dzone.com/articles/why-mongodb#:~:text=The%20motivation%20of%20the%20MongoDB,BSON%20documents%20to%20store%20data.
