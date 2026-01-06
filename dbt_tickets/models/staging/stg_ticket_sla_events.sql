{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_ticket_sla_events') }}
),

tipagem as (
    select
        -- IDs 
        {{ cast_int("payload ->> 'id'") }} as sla_event_id,
        {{ cast_int("payload ->> 'ticket_id'") }} as ticket_id,

        -- Dates
        {{ cast_timestamp("payload ->> 'time'") }} as event_time,
        
        -- Strings
        payload ->> 'metric' as metric,
        payload ->> 'type' as event_type,
        -- Demais campos
        payload -> 'sla' as sla
    from
        source
)

select * from tipagem