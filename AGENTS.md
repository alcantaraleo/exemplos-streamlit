# Regras para agentes (Cursor / assistentes de código)

## Idioma

- Usar **português** em respostas, código, comentários e documentação.
- Comentários no código e docstrings em português.
- Nomes de variáveis, funções e módulos em português quando apropriado ao domínio do projeto.

## Público-alvo e propósito

- Este repositório tem como propósito **ensinar programação para crianças e adolescentes entre 8 e 18 anos**.
- Toda decisão de código, documentação e interface deve priorizar o entendimento desse público.

## Documentação

- Toda documentação deve ser **explícita e clara**, com linguagem apropriada para o público-alvo (8 a 18 anos).
- Criar **README.md** em cada projeto/exemplo com instruções **claríssimas** para execução e estrutura do projeto.
- Priorizar sempre o entendimento de maneira **simples e clara**.

## Comentários no código

- Comentários devem ser **amigáveis** e explicar de maneira **simples e educacional**.
- Usar **muitos comentários** para explicar linhas de código, a lógica de programação e o que cada método faz.
- Objetivo: ajudar o aprendizado passo a passo.

## Nomes e funções

- Nomes de **funções** em **português**, com descrições claras.
- Priorizar o entendimento do público-alvo ao escolher nomes (evitar jargões desnecessários).

## Código e lógica (Streamlit)

- O repositório contém **exemplos e aplicações em Streamlit**.
- Usar **lógica simples** mesmo que o código fique mais extenso.
- **Não utilizar** lógicas complexas que exijam conhecimento profundo de programação.
- Preferir passos explícitos e fáceis de seguir.

## Visual e interface

- Os exemplos devem ser **coloridos e visualmente atrativos**, adequados ao público-alvo (crianças e adolescentes).

## Conventional Commits

Use o padrão [Conventional Commits](https://www.conventionalcommits.org/) para todas as mensagens de commit:

| Prefixo | Quando usar | Exemplo |
|---------|-------------|---------|
| `feat:` | Nova funcionalidade | `feat: adiciona página de login` |
| `fix:` | Correção de bug | `fix: corrige validação de email` |
| `docs:` | Documentação | `docs: atualiza README do template MVP` |
| `refactor:` | Refatoração sem mudar comportamento | `refactor: simplifica lógica do dashboard` |
| `style:` | Formatação, espaços, sem mudança de lógica | `style: organiza importações` |
| `chore:` | Tarefas de manutenção, dependências | `chore: atualiza requirements.txt` |

Exemplo de mensagem completa:
```
feat: adiciona validação de email no login

Verifica se o email contém "@" e "." para evitar entradas inválidas.
```
