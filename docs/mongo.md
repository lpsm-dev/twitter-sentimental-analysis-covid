# Intrudução ao MongoDB

O MongoDB é um banco de dados de documentos projetado para facilitar o desenvolvimento e o dimensionamento.

## Banco de dados de Documentos

Um registro no MongoDB é um documento, que é uma estrutura de dados

## Commandos

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
