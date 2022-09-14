-- все инженеры, приоритет доступа к товарам которых выше 10
 select e.name, 
 	e."birth year", 
 	ps.name as "position", 
 	pr.number as "priority" 
from emploees e 
left join positions ps on ps.id = e.position 
left join priorities pr on e.priority = pr.id 
where pr.number < 10 and ps.name = 'Инженер'
order by e.name 
