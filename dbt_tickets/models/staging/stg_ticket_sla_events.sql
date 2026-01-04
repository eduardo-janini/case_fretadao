{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_ticket_sla_events') }}
),

tipagem as (
    select
        -- IDs 
        (payload ->> 'id')::int as ticket_sla_event_id,
        (payload ->> 'ticket_id')::int as ticket_id,

        -- Dates
        (payload ->> 'time')::timestamp as time,
        
        -- Strings
        payload ->> 'metric' as metric,
        payload ->> 'type' as type,

        -- Demais campos
        payload -> 'sla' as sla
    from
        source
)

select * from tipagem

"metric": "reply_time",
"type": "fulfill"