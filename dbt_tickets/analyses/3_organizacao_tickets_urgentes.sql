select
    o.organization_name,
    count(distinct t.ticket_id) as total_urgent_tickets
from
    {{ ref("fat_tickets")}} as t
        inner join {{ ref("dim_organizations")}} as o using(organization_id)
where
    t.priority = 'urgent'
    and organization_id is not null
group by
    organization_name
order by
    total_urgent_tickets desc
limit 1