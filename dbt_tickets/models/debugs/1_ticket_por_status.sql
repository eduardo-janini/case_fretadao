select
    ticket_status,
    count(*) as total_tickets
from
    {{ ref('int_tickets') }}
group by
    ticket_status
order by
    total_tickets desc