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
