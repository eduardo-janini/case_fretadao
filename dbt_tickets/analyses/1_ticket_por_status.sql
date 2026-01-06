select
    ticket_status,
    count(distinct ticket_id) as total_tickets
from
    {{ ref('fat_tickets') }}
group by
    ticket_status
order by
    total_tickets desc