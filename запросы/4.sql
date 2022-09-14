select 
	e.name,
	c.name as "place of work"
from emploees e
inner join emploees_stocks e_s on e_s.emploee_id = e.id
inner join stocks s on s.id = e_s.stock_id
left join countries c on c.id = s.country
order by e.name