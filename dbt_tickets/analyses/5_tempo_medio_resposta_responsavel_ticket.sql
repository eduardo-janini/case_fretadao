select
    t.assignee_id,
    avg(tm.reply_time_in_minutes) as avg_reply_time_in_minutes
from
    {{ ref("stg_ticket_metrics")}} as tm
    inner join {{ ref("int_tickets")}} as t using(ticket_id)
group by
    t.assignee_id
order by
    avg_reply_time_in_minutes desc