{{ config(
    materialized='table',
    unique_key='ticket_metric_id',
    tags=['fact']
) }}

select
    ticket_metric_id,
    ticket_id,
    created_at,
    assigned_at,
    assignee_updated_at,
    solved_at,
    on_hold_time_in_minutes,
    reopens,
    replies,
    reply_time_in_minutes,
    requester_wait_time_in_minutes,
    satisfaction_score
from
    {{ ref('stg_ticket_metrics') }}