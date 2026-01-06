{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_ticket_metrics') }}
),

tipagem as (
    select
        -- IDs 
        {{ cast_int("payload ->> 'id'") }} as ticket_metric_id,
        {{ cast_int("payload ->> 'ticket_id'") }} as ticket_id,

        -- Dates
        {{ cast_timestamp("payload ->> 'created_at'") }} as created_at,
        {{ cast_timestamp("payload ->> 'assigned_at'") }} as assigned_at,
        {{ cast_timestamp("payload ->> 'assignee_updated_at'") }} as assignee_updated_at,
        {{ cast_timestamp("payload ->> 'solved_at'") }} as solved_at,

        -- Ints
        {{ cast_int("payload ->> 'on_hold_time_in_minutes'") }} as on_hold_time_in_minutes,
        {{ cast_int("payload ->> 'reopens'") }} as reopens,
        {{ cast_int("payload ->> 'replies'") }} as replies,
        {{ cast_int("payload ->> 'reply_time_in_minutes'") }} as reply_time_in_minutes,
        {{ cast_int("payload ->> 'requester_wait_time_in_minutes'") }} as requester_wait_time_in_minutes,
        {{ cast_int("payload ->> 'satisfaction_score'") }} as satisfaction_score
    from
        source
)

select * from tipagem
