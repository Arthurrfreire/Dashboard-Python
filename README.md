# Painel de Dados em Tempo Real para Ciência de Dados

![](https://i.imgur.com/QCJbLu3.png)

Este painel interativo em tempo real oferece uma visão dinâmica e atualizada de dados relacionados a marketing bancário. Ele permite explorar e analisar informações sobre clientes, como idade, estado civil, saldo de conta e profissão.

## Sumário

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Componentes do Painel](#componentes-do-painel)
- [Dependências](#dependências)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Recursos

- **Visualização Dinâmica:** Atualize os dados em tempo real para acompanhar as mudanças.
- **Filtros Interativos:** Selecione a profissão de interesse para visualizar dados específicos.
- **Métricas-Chave (KPIs):** Acompanhe a média de idade, número de casados e saldo médio por conta.
- **Gráficos Informativos:** Explore a distribuição de idade por estado civil e o histograma de idades.
- **Visualização Detalhada:** Acesse uma tabela completa com os dados filtrados.

## Instalação

1. **Clone o Repositório:**
   ```bash
   git clone <repositório-url>
   cd nome-do-repositório
2. **Crie um Ambiente Virtual (Recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate 
3. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt

## Uso
1. **Execute o Painel:**
   ```bash
   streamlit run app.py

2. **Acesse no Navegador: O painel estará disponível em http://localhost:8501.**

3. **Interaja com o Painel:**

- Utilize o menu suspenso para selecionar a profissão.
- Clique no botão "Atualizar Dados" para simular a atualização dos dados.
- Explore os gráficos e a tabela de dados detalhada.

## Componentes do Painel

   - **Filtro de Profissão:** Permite selecionar a profissão para análise.

   - **Métricas-Chave:** Exibe a média de idade, número de casados e saldo médio por conta.

   - **Gráfico de Mapa de Calor:** Mostra a distribuição de idade por estado civil.

   - **Histograma:** Apresenta a distribuição das idades.

   - **Tabela de Dados:** Detalhes dos dados filtrados por profissão.

## Dependências

 - Pandas
 - Plotly
 - NumPy
 - Streamlit
   
## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.

## Licença
Este projeto está licenciado sob a MIT License.
