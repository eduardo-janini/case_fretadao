# Case Analytics Engineer III

## Arquitetura
API → RAW → STAGING → INTERMEDIATE → MARTS → ANALYSES

## Key Decisions
- Ingestão incremental usando `start_time` da API
- Atualização completa para entidades tipo dimensão
- Camada raw apenas para anexação com deduplicação em staging
- Tipagem rigorosa e macros dbt reutilizáveis
- Modelos intermediários apenas para dados aninhados ou baseados em eventos

## Como rodar
1. docker compose up
2. python -m raw_layer.run_all
    - python -m raw_layer.drop_tables: Adicionei um script para dropar a camada raw, e por consequência, as view dependentes
3. dbt run
4. dbt test
5. dbt docs serve