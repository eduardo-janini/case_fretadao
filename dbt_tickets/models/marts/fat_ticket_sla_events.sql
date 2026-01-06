{{ config(
    materialized='table',
    unique_key='sla_event_id',
    tags=['fact']
) }}

select
    sla_event_id,
    ticket_id,
    event_time,
    metric,
    event_type,
    sla_policy_id,
    sla_policy_title
from
    {{ ref('int_ticket_sla_events') }}