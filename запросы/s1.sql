SELECT 
	items.id, 
	items.name, 
	t.name as "type",
	s.name as "stock name",
	s.latitude as "stock latitude",
	s.longitude as "stock longitude",
	items.arrival_time, 
	items.arrival_date, 
	p."Name" as "point of departure",
	o."name" as "departude company name"
FROM public.items
left join stocks s on s.id = items.stock
left join places p on p.id = items."point of departure"
left join types t on t.id = items.type
left join organizations o on o.id = p."Organization"
order by items.arrival_date, items.arrival_time