{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_ticket_metrics') }}
),

tipagem as (
    select
        -- IDs 
        (payload ->> 'id')::int as ticket_metrics_id,
        (payload ->> 'ticket_id')::int as ticket_id,

        -- Dates
        (payload ->> 'created_at')::timestamp as created_at,
        (payload ->> 'assigned_at')::timestamp as assigned_at,
        (payload ->> 'assignee_updated_at')::timestamp as assignee_updated_at,
        (payload ->> 'solved_at')::timestamp as solved_at,

        -- Ints
        (payload ->> 'on_hold_time_in_minutes')::int as on_hold_time_in_minutes,
        (payload ->> 'reopens')::int as reopens,
        (payload ->> 'replies')::int as replies,
        (payload ->> 'reply_time_in_minutes')::int as reply_time_in_minutes,
        (payload ->> 'requester_wait_time_in_minutes')::int as requester_wait_time_in_minutes,
        (payload ->> 'satisfaction_score')::int as satisfaction_score
    from
        source
)

select * from tipagem
