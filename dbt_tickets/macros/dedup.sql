-- dbt_tickets/macros/dedup.sql
-- Este arquivo é uma macro do dbt que realiza a deduplicação de registros em uma tabela ou relação.
-- A macro utiliza a função row_number() para identificar e manter apenas o primeiro registro

{% macro dedup(
    relation,
    partition_by,
    order_by
) %}

select *
from (
    select
        *,
        row_number() over (
            partition by {{ partition_by | join(', ') }}
            order by {{ order_by | join(', ') }} desc
        ) as rn
    from {{ relation }}
) as deduped
where rn = 1

{% endmacro %}
