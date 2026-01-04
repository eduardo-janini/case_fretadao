select
    sla_event_id,
    ticket_id,
    time as event_time,
    metric,
    type as event_type,
    {{ cast_int("sla ->> 'policy_id'") }} as sla_policy_id,
    sla ->> 'policy_title'         as sla_policy_title
from
    {{ ref('stg_ticket_sla_events') }}
