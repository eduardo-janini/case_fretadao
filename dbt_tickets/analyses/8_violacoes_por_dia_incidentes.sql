select
    tse.event_time,
    count(distinct tse.sla_event_id) as total_violations
from
    {{ ref("fat_tickets") }} as t
        inner join {{ ref("fat_ticket_sla_events") }} as tse using(ticket_id)
where
    ticket_type = 'incident'
    and tse.event_type = 'breach'
group by
    tse.event_time
order by
    tse.event_time