texto = '''
# Relatório
---
## Título em nível 2
### Título em nível 3

* Texto em *itálico*
* Texto em **negrito**
*Texto em ***itálico e negrito***
* Texto ~~riscado~~

Para definir uma linha horizontal adicione pelo menos três asteriscos (*), traços (-) ou underline (_) ao início da linha
___

Para definir um parágrafo separe linhas de texto com uma linha vazia.

> Sou uma citação em bloco!

> Sou uma citação em bloco
>
>> E eu sou uma citação em bloco(aninhada)!

1. Primeiro
2. Segundo
3. Terceiro

* Primeiro
* Segundo
* Terceiro

- [ ] Tarefa 1 não realizada
- [x] Tarefa 2 realizada

Inclua a `hugo version` para obter a versão de Hugo

### Link
[Sou um link relativo a outra página (no mesmo diretório) do web site](image/)

[Sou um link relativo a outra página (página principal) do web site](./)

### imagem
![Sou uma imagem](/home/cid-ivan/machine/bagoftoolsfl/assets/images/logo.png)

### Tabelas
| Variável | Valor | Descrição |
| -------- | ----- | ----------- |
| A        | 1     | Inteiro     |
| B        | 2     |             |

### Emoji
Copia o emoji 🤘 e cola.

----
### Nota de rodapá
1. (referência da nota de rodapé) Para definir uma referência da nota de rodapé use a seguinte sintaxe:
> Texto_associado_a_nota_de_rodape[^Referência_da_nota_de_rodapé]

2. (conteúdo da nota de rodapé). Para definir o conteúdo da nota de rodapé use a seguinte sintaxe:
> [^Referência_da_nota_de_rodapé]: Conteúdo_da_nota_de_rodapé

**Exemplo**

Eu venho daqui[^1]

[^1]: Eu sou uma nota de rodapé



'''