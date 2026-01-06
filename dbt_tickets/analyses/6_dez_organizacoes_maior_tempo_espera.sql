select
    o.organization_name,
    sum(tm.on_hold_time_in_minutes) as total_on_hold_time_in_minutes
from
    {{ ref("fat_ticket_metrics")}} as tm
    inner join {{ ref("fat_tickets")}} as t using(ticket_id)
    inner join {{ ref("dim_organizations")}} as o using(organization_id)
group by
    o.organization_name
order by
    total_on_hold_time_in_minutes desc
limit 10