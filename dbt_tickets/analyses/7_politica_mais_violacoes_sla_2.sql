-- Não ficou claro se deveria quebrar por métrica
-- ou somente por política de SLA.
-- Optei por ambas as colunas nesse caso.

select
    tse.metric,
    tse.sla_policy_title,
    count(distinct tse.sla_event_id) as total_violations
from
    {{ ref("int_ticket_sla_events")}} as tse
where
    tse.event_type = 'breach'
group by
    tse.metric,
    tse.sla_policy_title
order by
    total_violations desc