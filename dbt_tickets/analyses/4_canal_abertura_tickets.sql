select
    t.channel,
    count(distinct t.ticket_id) as total_opened_tickets
from
    {{ ref("fat_tickets")}} as t
group by
    t.channel
order by 
    total_opened_tickets desc
limit 1