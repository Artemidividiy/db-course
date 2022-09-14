SELECT e.id, e.name, e."birth year", ps.name as "position", pr.number as "priority", s.name as "stock name", c.name as "stock country", s.longitude as "stock longitude", s.latitude as "stock latitude"
	FROM public.emploees e
inner join emploees_stocks e_s on e_s.emploee_id = e.id
inner join stocks s on s.id = e_s.stock_id
left join countries c on c.id = s.country
left join positions ps on ps.id = e.position
left join priorities pr on pr.id = e.priority
order by e.name, e.priority, c.name